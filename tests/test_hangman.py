from games.hangman import GAME_NAME, WORDS, is_solved, mask_word, play


def test_mask_word_no_guesses():
    assert mask_word("apple", set()) == "_____"


def test_mask_word_correct_guesses():
    assert mask_word("apple", {"a", "p"}) == "app__"


def test_mask_word_case_insensitive():
    assert mask_word("Apple", {"a", "P"}) == "App__"


def test_mask_word_with_korean():
    assert mask_word("apple", {"가", "a"}) == "a____"


def test_is_solved_true():
    assert is_solved("apple", {"a", "p", "l", "e"}) is True


def test_is_solved_false():
    assert is_solved("apple", {"a", "p"}) is False


def test_is_solved_case_insensitive():
    assert is_solved("Apple", {"A", "P", "L", "E"}) is True


def test_words_list_not_empty():
    assert len(WORDS) > 0


def test_game_name():
    assert GAME_NAME == "행맨"


def test_play_rejects_korean_input(monkeypatch, capsys):
    monkeypatch.setattr("random.choice", lambda _: "cat")
    answers = iter(["가", "c", "a", "t"])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))

    play()

    captured = capsys.readouterr().out
    assert "알파벳 한 글자만 입력하세요." in captured
    assert "축하합니다! 승리하셨습니다." in captured
