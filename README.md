# Number Guessing Game
## Overview
This is a simple Python command-line number guessing game. The player is prompted to guess a number between 1 and 100, and the program will provide feedback on whether the guess is too high, too low, or correct. The goal is to guess the number in as few attempts as possible.

### How It Works
1. The program generates a random number between 1 and 100.
2. The player inputs their guess.
3. The program provides feedback:
    * Too low: If the guess is lower than the target number.
    * Too high: If the guess is higher than the target number.
    * Correct: If the guess matches the target number.
4. The game ends when the player guesses the number correctly, and the number of attempts is displayed.

## Requirements
* Python 3.x
* `pytest` for testing
* `pycodestyle` for code style checks

## Installation
1. Clone this repository:
```
git clone https://github.com/Wise-deldu/PRODIGY_SD_02.git
```
2. Navigate into the project directory:
```
cd PRODIGY_SD_02
```
3. Install the required packages:
```
pip install pytest pycodestyle
```

## Usage
Run the game by executing the `guess_game.py` file:
```
python guess_game.py
```
You will be prompted to guess a number between 1 and 100. Keep guessing until you find the correct number.

## Testing
Unit tests are provided to ensure the game logic is working correctly. We use `pytest` for testing. To run the tests, use the following command:
```
pytest test_guess_game.py
```

### Example of Tests
* `test_guess_number_low():` Ensures that when the guess is lower than the target number, the game returns "Too low! Try again."
* `test_guess_number_high():` Ensures that when the guess is higher than the target number, the game returns "Too high! Try again."
* `test_guess_number_correct():` Ensures that when the guess matches the target number, the game returns the correct congratulatory message.
* `test_main():` Tests the main game loop by simulating user input and checking printed output.

# Author
[Wise D. Duho](https://github.com/Wise-deldu)
