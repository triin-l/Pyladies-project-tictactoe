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


# Answers
# a) Module is a collection of code which can be used in your own code after importing it.
#    Several modules together (in levels) make up the package
#
# b) Someone else's created module may contain its execution command and then importing it
#    causes it to be executed, for example a function to draw something will create a drawing upon import
#    To avoid it, one should add to the end of the code:
#    if __name__ == "__main__":
#        name_of_the_function()

# c) Exceptions can be raised when one predicts something that may go wrong with the execution of the code.
#    In that case, its not just a general error message which pops up, but a specific exception error,
#    showing exactly where the problem is.
#
# d) To create: "if", "while", to throw: "raise", to catch: "try", "except", "else", "finally"
#
# e) Writing tests forces you to think of everything that may go wrong with the code.
#    One can then, for example, add exceptions into the code to catch those problems.
