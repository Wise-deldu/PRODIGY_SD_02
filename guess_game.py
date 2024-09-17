#!/usr/bin/env python3
import random


def main():
    print("Welcome to the number Guessing Game!")
    print("====================================")

    target_num = random.randint(1, 10)

    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            attempts += 1

            if guess < target_num:
                print("Too low! Try again.")
            elif guess > target_num:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {target_num} "
                      f"correctly in {attempts} attempts")
                break
        except ValueError:
            print("Invalid input! Please enter an integer")


if __name__ == "__main__":
    main()
