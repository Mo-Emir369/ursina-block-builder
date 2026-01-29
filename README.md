# 🧱 Ursina Block Builder

A simple **Minecraft-like sandbox game** built with **Python** using the **Ursina Engine**.

This project was created as a **learning and portfolio project**, focusing on clean code, modular design, and core game mechanics rather than graphics or assets.

---

## 🎯 Project Goals

This project demonstrates my understanding of:

- Python programming fundamentals
- Object-Oriented Programming (OOP)
- Modular and scalable code structure
- Basic game mechanics and logic
- File handling (saving & loading data)
- Git & GitHub workflow

---

## ✨ Features

- First-person movement system
- Place and break blocks in a 3D world
- Hotbar block selection (1–9 + mouse scroll)
- Pause menu (ESC)
- Save and load worlds using JSON files
- Clean and modular project structure
- Easily extendable for new blocks or features

---

## 🎮 Controls

| Action | Key |
|------|----|
| Move | W / A / S / D |
| Look around | Mouse |
| Jump | Space |
| Place block | Left Mouse Button |
| Break block | Right Mouse Button |
| Select block | Mouse Scroll or 1–9 |
| Save world | F5 |
| Load world | F9 |
| Pause Menu | ESC |

---

## 📁 Project Structure

```
.
├─ main.py          # Game entry point
├─ world.py         # World and block management
├─ blocks.py        # Block definitions
├─ save_system.py   # Save & load logic (JSON)
├─ ui.py            # Hotbar and UI elements
├─ pause_menu.py    # Pause menu logic
├─ requirements.txt # Project dependencies
└─ worlds/          # Saved worlds

````

---

## 🧩 Assets

Game assets (textures and sounds) are **not included** in this repository.

This is intentional — the project focuses on:
- Code structure
- Game logic
- System design

You can use any **free voxel-style textures or sounds** to run and customize the project.

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Mo-Emir369/ursina-block-builder.git
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the game:

   ```bash
   python main.py
   ```

---

## 💡 Inspiration & Credits

Inspired by early Minecraft-style prototypes, including:
[https://github.com/beaucarnes/zizyo](https://github.com/beaucarnes/zizyo)

The codebase, structure, and features were **significantly rewritten and extended**.

---

## 📜 License

This project is licensed under the **MIT License**.

```
