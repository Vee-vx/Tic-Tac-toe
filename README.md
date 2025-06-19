# 🎮 Python Tic-Tac-Toe Game (Noughts and Crosses)

This is a Python console application for playing the classic **Tic-Tac-Toe** (also known as Noughts and Crosses) game. The project was developed as part of the **DOC 334 – Computer Programming** module at IIT for the **Foundation Certificate in Higher Education**.

---

## 📌 Features

- 🧑‍🤝‍🧑 Two-player mode: Player 1 is `X`, Player 2 is `O`
- 📋 Tracks wins, losses, and draws for each session
- 🧠 Intelligent turn handling and win detection
- 🧼 Clear console interface after each move
- 📝 Game history and statistics saved in `.txt` files
- 🌐 Results automatically exported to an `index.html` file

---

## 📁 Project Structure
📦 TicTacToe-Game
├── Tic_Tac_Toe.py # Main game script
├── helper.py # Helper functions
├── index.html # Web view of game stats
├── current_session.txt # Keeps track of session number
├── session_1_stats.txt # Stats for session 1 (example)
├── session_1_history.txt # History of moves for session 1 (example)

---

## ▶️ How to Run

1. Make sure Python 3 is installed on your computer.
2. Clone the repository or download the files.
3. Open a terminal in the project directory.
4. Run the game using:

```bash
python Tic_Tac_Toe.py
🔧 Modules Used
os – for file handling and clearing the console.

No third-party libraries required.

🧪 Test Cases
Test Case	Description	Input	Expected Output
1	Start game	Option 1	Game board shown
2	Exit game	Option 3	Program terminates
3	Invalid main menu choice	Invalid key	"Invalid choice" message
4	Quit mid-game	Q	Return to main menu
5	Input invalid grid number	e.g. 11	"Invalid position" message
6	Use already taken spot	Used cell	"Invalid position" message
7	Non-number input during game	A or !	"Invalid position" message
8	Draw game	Full board	"Game is Tied!"
9	Player 1 wins	Correct seq	"Player 1/X wins!"
10	Player 2 wins	Correct seq	"Player 2/O wins!"

📊 Output
Console-based game interaction

Session summaries saved to:

session_<n>_stats.txt

session_<n>_history.txt

index.html generated to view results in a browser

👨‍💻 Developer Info
Name: Vihanga Visalka

Student ID: 20232519

Module Leader: Mr. Nishan Saliya

Tutorial Support: Ms. Shafka Fuard

Institute: IIT (Informatics Institute of Technology)

University Affiliation: University of Westminster

Assignment Type: Individual Coursework

📝 License
This project is for academic purposes. You may use or modify it freely for learning.

If you use parts of this code in your own work, please provide appropriate credit.

🎓 "Developed as part of the DOC 334 programming module at IIT – 2024."
