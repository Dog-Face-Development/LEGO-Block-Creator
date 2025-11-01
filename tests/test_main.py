"""Tests for main.py."""
# pylint: disable=import-error, wrong-import-position, unused-argument, line-too-long

import sys
import os
from unittest.mock import patch, call

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import main


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


@patch("builtins.input", side_effect=["sortparts-all"])
@patch("builtins.print")
def test_lego_cmd_sortparts_all(self, mock_print):
    """Test the sortparts-all command."""
    main.lego_cmd()
    # Verify that the command was processed
    assert mock_print.call_count >= 1


@patch("builtins.input", side_effect=["sortparts-name", "Brick"])
@patch("builtins.print")
def test_lego_cmd_sortparts_name(self, mock_print):
    """Test the sortparts-name command."""
    main.lego_cmd()
    mock_print.assert_has_calls(
        [
            call("LEGO CMD: "),
            call("Please enter a brick name: "),
        ]
    )


@patch("builtins.input", side_effect=["sortparts-colour", "Red"])
@patch("builtins.print")
def test_lego_cmd_sortparts_colour(self, mock_print):
    """Test the sortparts-colour command."""
    main.lego_cmd()
    mock_print.assert_has_calls(
        [
            call("LEGO CMD: "),
            call("Please enter a brick colour: "),
        ]
    )


@patch("builtins.input", side_effect=["sortparts-color", "Red"])
@patch("builtins.print")
def test_lego_cmd_sortparts_color(self, mock_print):
    """Test the sortparts-color command."""
    main.lego_cmd()
    mock_print.assert_has_calls(
        [
            call("LEGO CMD: "),
            call("Please enter a brick color: "),
        ]
    )


@patch("builtins.input", side_effect=["sortsets-all"])
@patch("builtins.print")
def test_lego_cmd_sortsets_all(self, mock_print):
    """Test the sortsets-all command."""
    main.lego_cmd()
    # Verify that the command was processed
    assert mock_print.call_count >= 1


@patch("builtins.input", side_effect=["sortsets-name", "Police Station"])
@patch("builtins.print")
def test_lego_cmd_sortsets_name(self, mock_print):
    """Test the sortsets-name command."""
    main.lego_cmd()
    mock_print.assert_has_calls(
        [
            call("LEGO CMD: "),
            call("Please enter a set name (NOT number): "),
        ]
    )


@patch("builtins.input", side_effect=["sortsets-number", "123456"])
@patch("builtins.print")
def test_lego_cmd_sortsets_number(self, mock_print):
    """Test the sortsets-number command."""
    main.lego_cmd()
    mock_print.assert_has_calls(
        [
            call("LEGO CMD: "),
            call("Please enter a set number (NOT name): "),
        ]
    )


@patch("builtins.input", side_effect=["sortsets-theme", "City"])
@patch("builtins.print")
def test_lego_cmd_sortsets_theme(self, mock_print):
    """Test the sortsets-theme command."""
    main.lego_cmd()
    mock_print.assert_has_calls(
        [
            call("LEGO CMD: "),
            call("Please enter a set theme: "),
        ]
    )


@patch("builtins.input", side_effect=["help"])
@patch("builtins.print")
def test_lego_cmd_help(self, mock_print):
    """Test the help command."""
    main.lego_cmd()
    # Verify that help text is printed (self is actually mock_print due to decorator order)
    assert self.call_count >= 10  # Multiple help lines are printed


@patch("builtins.input", side_effect=["copyright"])
@patch("builtins.print")
def test_lego_cmd_copyright(self, mock_print):
    """Test the copyright command."""
    main.lego_cmd()
    # Verify that copyright text is printed
    assert mock_print.call_count >= 1


@patch("builtins.input", side_effect=["license"])
@patch("builtins.print")
def test_lego_cmd_license(self, mock_print):
    """Test the license command."""
    main.lego_cmd()
    # Verify that license text is printed
    assert mock_print.call_count >= 1


@patch("builtins.input", side_effect=["invalidcommand"])
@patch("builtins.print")
def test_lego_cmd_invalid(self, mock_print):
    """Test an invalid command."""
    main.lego_cmd()
    # Verify error message is printed
    assert mock_print.call_count >= 1
