"""숫자 야구 게임 테스트 — 담당: C"""

from games import baseball


def test_make_answer():
    """정답이 중복 없는 숫자 3개인지 검사"""
    for _ in range(100):
        answer = baseball.make_answer()
        assert len(answer) == 3
        assert answer.isdigit()
        assert len(set(answer)) == 3


def test_three_strikes():
    assert baseball.judge("123", "123") == (3, 0)


def test_three_balls():
    assert baseball.judge("123", "231") == (0, 3)


def test_one_strike_two_balls():
    assert baseball.judge("123", "132") == (1, 2)


def test_out():
    assert baseball.judge("123", "456") == (0, 0)


def test_valid_guess():
    assert baseball.valid_guess("123")
    assert baseball.valid_guess("012")


def test_invalid_guess():
    assert not baseball.valid_guess("112")
    assert not baseball.valid_guess("12")
    assert not baseball.valid_guess("1234")
    assert not baseball.valid_guess("abc")
    assert not baseball.valid_guess("1a3")


def test_win(monkeypatch, capsys):
    """정답을 맞히면 게임이 정상 종료되는지 검사"""
    monkeypatch.setattr(baseball, "make_answer", lambda: "123")
    monkeypatch.setattr("builtins.input", lambda _: "123")

    assert baseball.play() is None

    output = capsys.readouterr().out
    assert "정답입니다!" in output


def test_nine_attempts(monkeypatch, capsys):
    """9번 실패하면 정답을 공개하는지 검사"""
    monkeypatch.setattr(baseball, "make_answer", lambda: "123")
    monkeypatch.setattr("builtins.input", lambda _: "456")

    assert baseball.play() is None

    output = capsys.readouterr().out
    assert output.count("아웃!") == 9
    assert "정답은 123" in output


def test_invalid_input_not_counted(monkeypatch, capsys):
    """잘못된 입력은 도전 횟수에 포함하지 않음"""
    monkeypatch.setattr(baseball, "make_answer", lambda: "123")

    guesses = iter(["112", "123"])
    monkeypatch.setattr("builtins.input", lambda _: next(guesses))

    baseball.play()

    output = capsys.readouterr().out
    assert "잘못된 입력입니다." in output
    assert "1번 만에" in output
