
# Python Number Guessing Game 🎯

A feature-rich, interactive terminal-based number guessing game built in Python. Challenge yourself across three difficulty levels, track your performance with detailed statistics, and discover your most frequently guessed number using SciPy's mode calculation.

## Features

- **Three Difficulty Levels:**
  - **Easy:** Guess a number between 1 and 5 with 3 lives.
  - **Medium:** Guess a number between 1 and 10 with 4 lives.
  - **Hard:** Guess a number between 1 and 20 with 5 lives.
- **Dynamic Lives System:** Each incorrect guess costs you a life. Lose all lives, and the game ends.
- **Comprehensive Statistics:** Tracks total games played, wins, losses, and win percentage across your entire session.
- **Guess History:** Stores every guess you make throughout the session.
- **Best & Worst Game Tracking:** Compares how many attempts each game took and shows your fewest-attempt (best) and most-attempt (worst) games.
- **Mode Analysis:** Utilizes `scipy.stats.mode` to calculate and display the most frequently guessed number.
- **Continuous Play:** After each round, choose to continue playing or quit without restarting the script.
- **Error Handling:** Gracefully handles invalid inputs (non-integers, wrong menu options) without crashing or losing your stats.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- SciPy library. Install it using pip:
  ```bash
  pip install scipy
  ```

### Running the Game

```bash
python guessing_game.py
```

## How to Play

1. Pick a difficulty: `e` for easy, `m` for medium, or `h` for hard.
2. Enter a whole number within that difficulty's range.
3. If you're right, you win the round. If you're wrong, you lose a life and get a hint (too high or too low).
4. Run out of lives, and the round ends.
5. After each round, choose `c` to play again or `q` to quit.
6. When you quit, your full session stats print out, including your best and worst games.
