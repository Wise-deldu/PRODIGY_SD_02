#!/usr/bin/env python3
import random


def guess_number(target_num, guess):
    if guess < target_num:
        return "Too low! Try again."
    if guess > target_num:
        return "Too high! Try again."
    else:
        return (
            f"Congratulations! You guessed the number {target_num} correctly."
        )


def main():
    print("Welcome to the number Guessing Game!")
    print("====================================")

    target_num = random.randint(1, 100)

    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            result = guess_number(target_num, guess)
            print(result)

            if "Congratulations" in result:
                print(f"You guessed the number in {attempts} attempts")
                break
        except ValueError:
            print("Invalid input! Please enter an integer")


if __name__ == "__main__":
    main()
