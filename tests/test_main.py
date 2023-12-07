"""Tests for main.py."""
# pylint: disable=import-error, wrong-import-position, unused-argument, line-too-long

import main
import sys
import os
from unittest.mock import patch, call

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@patch("builtins.input", side_effect=["newpiece", "Brick", "Red", "5"])
@patch("builtins.print")
def test_lego_cmd_newpiece(self, mock_print):
    """Test the newpiece command."""
    main.lego_cmd()
    mock_print.assert_has_calls(
        [
            call("LEGO CMD: "),
            call("Name the piece you would like to add: "),
            call(
                'What is the piece colour                     (make sure this colour is in the colour database,                         otherwise add using "newcolour")? '
            ),
            call("How many of that would you like to add? "),
        ]
    )


@patch("builtins.input", side_effect=["newcolour", "Red"])
@patch("builtins.print")
def test_lego_cmd_newcolour(self, mock_print):
    """Test the newcolour command."""
    main.lego_cmd()
    mock_print.assert_has_calls(
        [
            call("LEGO CMD: "),
            call("Name the colour you would like to add: "),
        ]
    )


@patch("builtins.input", side_effect=["newcolor", "Red"])
@patch("builtins.print")
def test_lego_cmd_newcolor(self, mock_print):
    """Test the newcolor command."""
    main.lego_cmd()
    mock_print.assert_has_calls(
        [
            call("LEGO CMD: "),
            call("Name the color you would like to add: "),
        ]
    )


@patch("builtins.input", side_effect=["addpiece", "Brick", "Red", "5"])
@patch("builtins.print")
def test_lego_cmd_addpiece(self, mock_print):
    """Test the addpiece command."""
    main.lego_cmd()
    mock_print.assert_has_calls(
        [
            call("LEGO CMD: "),
            call("What is the name of the piece that you would like to add to? "),
            call("What is the piece colour? "),
            call("How many of that piece do you want to add? "),
        ]
    )


@patch("builtins.input", side_effect=["removepiece", "Brick", "Red", "5"])
@patch("builtins.print")
def test_lego_cmd_removepiece(self, mock_print):
    """Test the removepiece command."""
    main.lego_cmd()
    mock_print.assert_has_calls(
        [
            call("LEGO CMD: "),
            call("What is the name of the piece that you would like to remove? "),
            call("What is the piece colour? "),
            call("How many of that piece do you want to remove? "),
        ]
    )


@patch(
    "builtins.input",
    side_effect=["newset", "Police Station", "123456", "City", "100", "5"],
)
@patch("builtins.print")
def test_lego_cmd_newset(self, mock_print):
    """Test the newset command."""
    main.lego_cmd()
    mock_print.assert_has_calls(
        [
            call("LEGO CMD: "),
            call("Name the set you would like to add: "),
            call("What is the set number for the set you would like to add? "),
            call(
                'What is the theme for the set you would like to add? \
                    (make sure this theme is in the database, \
                        otherwise add using "newtheme") '
            ),
            call("How many pieces are there in this set? "),
            call("How many of this set would you like to add? "),
        ]
    )


@patch("builtins.input", side_effect=["newtheme", "City"])
@patch("builtins.print")
def test_lego_cmd_newtheme(self, mock_print):
    """Test the newtheme command."""
    main.lego_cmd()
    mock_print.assert_has_calls(
        [
            call("LEGO CMD: "),
            call("Name the theme you would like to add: "),
        ]
    )


@patch("builtins.input", side_effect=["addset", "123456", "5"])
@patch("builtins.print")
def test_lego_cmd_addset(self, mock_print):
    """Test the addset command."""
    main.lego_cmd()
    mock_print.assert_has_calls(
        [
            call("LEGO CMD: "),
            call("What is the set number of the set that you would like to add? "),
            call("How many of that set do you want to add? "),
        ]
    )


@patch("builtins.input", side_effect=["removeset", "123456", "5"])
@patch("builtins.print")
def test_lego_cmd_removeset(self, mock_print):
    """Test the removeset command."""
    main.lego_cmd()
    mock_print.assert_has_calls(
        [
            call("LEGO CMD: "),
            call("What is the set number of the set that you would like to remove? "),
            call("How many of that set do you want to remove? "),
        ]
    )
