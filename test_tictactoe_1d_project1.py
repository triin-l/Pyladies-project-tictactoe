import tictactoe_1d_project1
import pytest


def test_evaluate_winning():
    assert tictactoe_1d_project1.evaluate("--------xxx---------") == "x"


def test_evaluate_empty_space():
    assert tictactoe_1d_project1.evaluate("------------x-o--x-x") == "-"


def test_evaluate_end():
    assert tictactoe_1d_project1.evaluate("xxooxoxxoxooxoxooxo") == "!"


def test_move_general():
    assert tictactoe_1d_project1.move("--------------------", "x", 19)


def test_move_failure():
    with pytest.raises(ValueError):
        tictactoe_1d_project1.move("--------xx---x-x-x-x", "x", -2)
