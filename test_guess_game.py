import pytest
from unittest import mock
from guess_game import guess_number, main


def test_guess_number_low():
    assert guess_number(50, 30) == "Too low! Try again."


def test_guess_number_high():
    assert guess_number(50, 70) == "Too high! Try again."


def test_guess_number_correct():
    assert guess_number(50, 50) == (
        "Congratulations! You guessed the number 50 correctly."
    )


# Test for main using mock for input/output
@mock.patch('builtins.input', side_effect=[30, 50])
@mock.patch('builtins.print')
def test_main(mock_print, mock_input):
    with mock.patch('random.randint', return_value=50):
        main()

        # Check if success message is printed
        mock_print.assert_any_call(
            "Congratulations! You guessed the number 50 correctly."
            )
        mock_print.assert_any_call("You guessed the number in 2 attempts")
