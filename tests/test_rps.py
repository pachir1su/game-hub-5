import pytest

from games import rps


@pytest.mark.parametrize(
    "player, computer, expected",
    [
        ("가위", "보", "win"),
        ("바위", "가위", "win"),
        ("보", "바위", "win"),
        ("가위", "바위", "lose"),
        ("바위", "보", "lose"),
        ("보", "가위", "lose"),
        ("가위", "가위", "draw"),
        ("바위", "바위", "draw"),
        ("보", "보", "draw"),
    ],
)
def test_decide_all_combinations(player, computer, expected):
    assert rps.decide(player, computer) == expected


def test_decide_accepts_numbers():
    assert rps.decide("1", "3") == "win"
    assert rps.decide("2", "3") == "lose"
    assert rps.decide("3", "3") == "draw"


def test_decide_invalid_choice_raises():
    with pytest.raises(ValueError):
        rps.decide("사과", "보")


@pytest.mark.parametrize(
    "value, expected",
    [("1", "가위"), ("2", "바위"), ("3", "보"), (" 2 ", "바위")],
)
def test_normalize_valid(value, expected):
    assert rps.normalize(value) == expected


@pytest.mark.parametrize("value", ["", "0", "4", "abc", None, 3])
def test_normalize_invalid(value):
    assert rps.normalize(value) is None


def test_get_computer_choice_is_valid():
    for _ in range(50):
        assert rps.get_computer_choice() in rps.CHOICES


def test_is_match_over():
    assert not rps.is_match_over(0, 0)
    assert not rps.is_match_over(1, 1)
    assert rps.is_match_over(2, 0)
    assert rps.is_match_over(1, 2)


def _run_play(monkeypatch, inputs, computer_choices):
    inputs = iter(inputs)
    computers = iter(computer_choices)
    monkeypatch.setattr("builtins.input", lambda _="": next(inputs))
    monkeypatch.setattr(rps, "get_computer_choice", lambda: next(computers))
    rps.play()


def test_play_player_wins_two_rounds(monkeypatch, capsys):
    # 가위(vs 보) 승, 바위(vs 가위) 승 -> 2선승으로 종료
    _run_play(monkeypatch, ["1", "2"], ["보", "가위"])
    assert "최종 승리" in capsys.readouterr().out


def test_play_computer_wins_two_rounds(monkeypatch, capsys):
    _run_play(monkeypatch, ["1", "1"], ["바위", "바위"])
    assert "최종 패배" in capsys.readouterr().out


def test_play_draw_and_invalid_input_do_not_count(monkeypatch, capsys):
    # 잘못된 입력, 무승부 후 2연승
    _run_play(
        monkeypatch,
        ["x", "1", "1", "1"],
        ["가위", "보", "보"],
    )
    out = capsys.readouterr().out
    assert "잘못된 입력" in out
    assert "비겼습니다" in out
    assert "최종 승리" in out


def test_play_quit_returns_to_menu(monkeypatch, capsys):
    _run_play(monkeypatch, ["q"], [])
    assert "메인 메뉴로 돌아갑니다" in capsys.readouterr().out
