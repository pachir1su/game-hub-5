from games.hangman import mask_word, is_solved, WORDS, GAME_NAME


def test_mask_word_no_guesses():
    assert mask_word("apple", set()) == "_____"


def test_mask_word_correct_guesses():
    assert mask_word("apple", {"a", "p"}) == "app__"


def test_mask_word_case_insensitive():
    assert mask_word("Apple", {"a", "P"}) == "App__"


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