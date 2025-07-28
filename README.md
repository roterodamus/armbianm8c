## Armbianm8c

**Operating System for the R36S game console running only M8C based on Armbian.**  
This project replaces Arkm8c.

---

## 📥 Download Links

**Armbianm8c.tar.xz 1.0 - 371.1 MB (17-07-25)**  
- [Release Page](https://github.com/roterodamus/armbianm8c/releases)
- [Google Drive link](https://bit.ly/armbianm8c1)

---

## 🎮 Controls

- **D-pad**: Navigation
- **B**: Edit
- **A**: Options
- **Y or L2**: Shift
- **X or R2**: Play
- **R3 + Vol Up/Down**: Brightness Up/Down
- **Power Button**: Shut Down

### 🔑 Panel Picker Mode

To enter **Panel Picker Mode**, hold the correct button combination during boot:

**Hold the Hotkey (R1) + one of the following buttons while powering on:**

| R1 + Button | Panel # | Description                          |
|-------------|---------|--------------------------------------|
| **U**       | 1       | Panel 1                              |
| **R**       | 2       | Panel 2                              |
| **D**       | 3       | Panel 3                              |
| **L**       | 4       | Panel 4                              |
| **X**       | 5       | Panel 5 (Soy Sauce Console)         |
| **A**       | 0       | Original Panel (Stock)              |

---

## 📝 Notes, Tips, Bugs and Good to Know

- **Tested Panels**: Panel 5 (R36S Soy), Panel 4 (R36H)
- **Username**: `r36s`
- **Password**: `r36s`
- **CPU Governor**: Set to performance; your R36S might get hotter than usual.
- **Audio Issues**: Clicks and pops may occur, especially in the first 2 minutes. They should diminish after that.
- **Buffer Size**: You can set the buffer size in `~/jackm8c.sh`.
- **Stereo Channels**: Sometimes the stereo channels may be flipped.

---

## ⚙️ Installation Instructions

If you want to recreate this build, download [R36S-Armbian](https://github.com/R36S-Stuff/R36S-Armbian) and check out `install.sh`. Read it carefully and execute it on your R36S device. **DO NOT EXECUTE ON YOUR PC!** You will need to expand the file system first; a couple of GB is more than enough.

```bash
sudo apt install -y git
git clone https://github.com/roterodamus/armbianm8c.git
cd armbianm8c/
chmod +x install.sh 
./install.sh 
```

---

## 🙏 A Very Special Thanks To

- **Trash80** - [Dirtywave](https://dirtywave.com/)
- **And the creators of**:
  - [Laamaa / M8C](https://github.com/laamaa/m8c)
  - [EatPrilosec / Armbian for R36S](https://github.com/R36S-Stuff/R36S-Armbian)
  - [Christianhaitian / Arkos](https://github.com/christianhaitian/arkos)
  - [Drewsif / pishrink](https://github.com/Drewsif/PiShrink)
  - The entire FOSS Linux community.
