#!/usr/bin/env python3
import evdev
import subprocess
from evdev import InputDevice, categorize, ecodes
import threading
import time
import re

VOLUME_UP = 115
VOLUME_DOWN = 114
BTN_THUMBL = 317

# Devices
VOL_DEV = '/dev/input/event2'
THUMB_DEV = '/dev/input/event3'

# State
thumb_pressed = False
lock = threading.Lock()

def get_current_volume():
    result = subprocess.run(
        ['amixer', 'get', 'Master'],
        capture_output=True,
        text=True
    )
    matches = re.findall(r'\[(\d{1,3})%\]', result.stdout)
    return int(matches[0]) if matches else 0

def set_volume(new_volume):
    new_volume = max(0, min(new_volume, 100))  # Clamp to [0, 100]
    subprocess.run(['amixer', 'sset', 'Master', f'{new_volume}%'])

def adjust_volume(direction):
    current = get_current_volume()
    increment = 2
    if direction == '+':
        set_volume(current + increment)
    else:
        set_volume(current - increment)

def adjust_brightness(direction):
    path = '/sys/class/backlight/*/brightness'
    cmd = f"for f in {path}; do val=$(cat $f); new=$((val{'+5' if direction == '+' else '-5'})); echo $new | tee $f; done"
    subprocess.run(cmd, shell=True, executable='/bin/bash')

def monitor_thumb():
    global thumb_pressed
    dev = InputDevice(THUMB_DEV)
    for event in dev.read_loop():
        if event.type == ecodes.EV_KEY and event.code == BTN_THUMBL:
            with lock:
                thumb_pressed = event.value == 1

def monitor_volume():
    dev = InputDevice(VOL_DEV)
    for event in dev.read_loop():
        if event.type == ecodes.EV_KEY:
            with lock:
                if event.value == 1:
                    if event.code == VOLUME_UP:
                        if thumb_pressed:
                            adjust_brightness('+')
                        else:
                            adjust_volume('+')
                    elif event.code == VOLUME_DOWN:
                        if thumb_pressed:
                            adjust_brightness('-')
                        else:
                            adjust_volume('-')

if __name__ == '__main__':
    t1 = threading.Thread(target=monitor_thumb, daemon=True)
    t2 = threading.Thread(target=monitor_volume, daemon=True)
    t1.start()
    t2.start()
    while True:
        time.sleep(1)
