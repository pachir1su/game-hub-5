"""틱택토 핵심 로직 테스트."""

from games.tictactoe import EMPTY, check_winner, is_full, position_to_index


def test_check_winner_row():
    board = [
        ["X", "X", "X"],
        [EMPTY, "O", EMPTY],
        ["O", EMPTY, EMPTY],
    ]
    assert check_winner(board) == "X"


def test_check_winner_column():
    board = [
        ["O", "X", EMPTY],
        ["O", "X", EMPTY],
        ["O", EMPTY, "X"],
    ]
    assert check_winner(board) == "O"


def test_check_winner_diagonal():
    board = [
        ["X", "O", EMPTY],
        [EMPTY, "X", "O"],
        [EMPTY, EMPTY, "X"],
    ]
    assert check_winner(board) == "X"


def test_check_winner_none():
    board = [
        ["X", "O", EMPTY],
        [EMPTY, "X", EMPTY],
        ["O", EMPTY, EMPTY],
    ]
    assert check_winner(board) is None


def test_is_full():
    full_board = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["O", "X", "O"],
    ]
    not_full_board = [
        ["X", "O", EMPTY],
        ["O", "X", "O"],
        ["O", "X", "O"],
    ]

    assert is_full(full_board) is True
    assert is_full(not_full_board) is False


def test_position_to_index():
    assert position_to_index(1) == (0, 0)
    assert position_to_index(5) == (1, 1)
    assert position_to_index(9) == (2, 2)
