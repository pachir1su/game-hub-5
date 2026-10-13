"""공용 함수 테스트 예시."""

import utils


def test_ask_int_accepts_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "3")
    assert utils.ask_int("? ", 1, 5) == 3


def test_ask_int_retries_on_invalid(monkeypatch):
    answers = iter(["abc", "9", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    assert utils.ask_int("? ", 1, 5) == 2


def test_ask_yes_no(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Y")
    assert utils.ask_yes_no("계속?") is True


def test_ask_choice_accepts_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2")
    assert utils.ask_choice("? ", {"0", "1", "2"}) == "2"


def test_ask_choice_retries_on_invalid(monkeypatch):
    answers = iter(["9", "1"])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    assert utils.ask_choice("? ", {"0", "1"}) == "1"
