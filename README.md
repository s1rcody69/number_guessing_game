#  Number Guessing Game

A polished, console-based Python game where players challenge themselves to guess a secret number. This project features difficulty levels, smart hints, and a persistent leaderboard system using Python file handling.

## 👤Contributor
- **Cody May Odhiambo**

---

##  Overview
The **Number Guessing Game** is an interactive application that tests logic and probability. Unlike basic versions, this game tracks player performance over time by saving high scores to a local file, allowing for a competitive experience even after the program is closed.

---

##  Features
1.  **Dynamic Difficulty:** Choose between Easy (10 tries), Medium (7 tries), or Hard (5 tries).
2.  **Smart Hint System:** If you struggle for 3 turns, the game gives you a strategic hint (Even/Odd) to help you narrow down the secret number.
3.  **Persistent Leaderboard:** Uses Python's `File I/O` to save names and scores to `high_scores.txt`.
4.  **Top 5 Hall of Fame:** Automatically sorts and displays the top 5 players based on the fewest attempts.
5.  **Robust Logic:** Built with clean functions and error-handling to ensure a smooth experience.

---
## 🛠️ Tech Stack
*   **Language:** Python 3.12+
*   **Modules:** `random` (Number generation), `os` (File path management)
*   **Persistence:** Text-based file handling (`.txt`)
*   **Environment:** Console / Terminal

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/s1rcody69/number_guessing_game](https://github.com/s1rcody69/number_guessing_game)
   cd guessing_game