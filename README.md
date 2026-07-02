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
- **Mode Analysis:** Utilizes `scipy.stats.mode` to calculate and display the most frequently guessed number.
- **Continuous Play:** After each round, choose to continue playing or quit without restarting the script.
- **Error Handling:** Gracefully handles invalid inputs (non-integers, wrong menu options).

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- SciPy library. Install it using pip:

  ```bash
  pip install scipy