# armbianm8c
Operating System for the R36S game console running only M8C based on Armbian

## Download link:
Armbianm8c.tar.xz 0.1 - 435.2 MB
- [Google Drive link](https://bit.ly/armbianm8c)

## Controls:
- D-pad = Navigation
- B = Edit
- A = Options
- Y or L2 = Shift
- X or R2 = Play
- R3 + Vol Up or Down = Brightness Up or Down
- Power Button = shut down

To enter **Panel Picker Mode**, hold the correct button combination during boot:

**Hold the Hotkey (R1) + one of the following buttons while powering on:**

| R1 + Button | Panel # | Description             |
|-------------|---------|-------------------------|
| **U**       | 1       | Panel 1             |
| **R**       | 2       | Panel 2             |
| **D**       | 3       | Panel 3             |
| **L**       | 4       | Panel 4             |
| **X**       | 5       | Panel 5 (Soy Sauce Console)    |
| **A**       | 0       | Original Panel (Stock)  |

## Notes, tips and GoodToKnows:

username: r36s
password: r36s

you can set buffersize in ~/jackm8c.sh

### install.sh

if you want to recreate this build, check out install.sh. read it (I have not tested it yet, but its pretty straight forward), and execute on your r36s device. DO NOT EXECUTE ON YOUR PC!
you will have to expand the file system first, couple of gb is more than enough.

```bash
sudo apt install -y git
git clone https://github.com/roterodamus/armbianm8c.git
cd armbianm8c/
chmod +x install.sh 
./install.sh 
```

## A very special thanks to:

- Trash80 - [Dirtywave](https://dirtywave.com/)

### and to the creators of:
- [M8C](https://github.com/laamaa/m8c)
- [EatPrilosec / Armbian for R36S](https://github.com/R36S-Stuff/R36S-Armbian)
- [arkos](https://github.com/christianhaitian/a...)
- [pishrink](https://github.com/Drewsif/PiShrink)
- and the entire FOSS Linux community.
