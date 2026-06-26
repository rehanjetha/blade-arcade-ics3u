# Blade Arcade

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/UI-Tkinter-22D3EE?style=for-the-badge)
![PyBoy](https://img.shields.io/badge/Optional-PyBoy-F472B6?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-FACC15?style=for-the-badge)

Blade Arcade is a Grade 11 ICS3U computer science project built with Python and
Tkinter. It combines a local login screen, a shared coin balance, two
terminal-based mini-games, and an optional Game Boy emulator section that uses
PyBoy.

The goal of the project was to practice Python fundamentals, basic GUI design,
JSON file storage, modular code organization, and connecting several smaller
programs into one arcade-style app.

## At a Glance

| Area | What it does |
| --- | --- |
| Login | Creates local accounts and signs users in through a Tkinter screen |
| Coins | Stores and updates each user's coin balance in JSON |
| Free games | Runs HighLow Gamble and Duck, Fish, Mosquito in the terminal |
| Emulator | Optionally launches Game Boy ROMs through PyBoy |
| Saves | Writes per-user game saves and activity logs locally |

## Project Structure

```text
Blade Arcade/
├── Control/              # Shared helpers for buttons and coins
├── Database/             # Local user data and generated logs
├── Games/                # Mini-games and PyBoy integration
├── Pages/                # Tkinter login and home screens
├── Resources/            # Icons and GUI image assets
├── ROMs/                 # User-provided ROM files only
├── Saves/                # Generated save states
└── Jetha_Rehan_Arcade.py # Main entry point
```

## Requirements

- Python 3
- Pillow
- PyBoy

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Running the App

Start the arcade with:

```bash
python Jetha_Rehan_Arcade.py
```

On the login screen, create a new local account with the sign-up button. The
account data is stored locally in `Database/users.json`.

Tkinter can render native controls differently across Windows and macOS, so the
exact button styling may vary by operating system.

## ROMs

ROM files are not included in this repository.

To use the emulator buttons, place legally owned Game Boy ROM files in the
`ROMs/` folder with these names:

```text
ROMs/mario.gb
ROMs/tetris.gb
```

The rest of the arcade can still be viewed without adding ROM files.

## Notes

This is a student project, not a production login or account system. Passwords
and coins are stored locally in JSON so the program can stay simple and easy to
inspect.

## License

This project is released under the MIT License.
