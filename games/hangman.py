"""행맨 — 담당: B

규칙
- 단어 하나를 고른다.
- 플레이어는 한 글자씩 추측한다.
- 틀리면 기회가 1 줄어든다. 기본 기회는 6번.
- 맞힌 글자만 보여 준다.

구현 힌트
- mask_word(word: str, guessed: set[str]) -> str
- is_solved(word: str, guessed: set[str]) -> bool
"""

import random

GAME_NAME = "행맨"

WORDS = [
    "apple",
    "banana",
    "orange",
    "python",
    "programming",
    "computer",
    "hangman",
    "developer",
    "keyboard",
    "guitar",
]


def mask_word(word: str, guessed: set[str]) -> str:
    """맞힌 글자만 보여 주고 나머지는 '_'로 마스킹한다."""
    guessed_lower = {g.lower() for g in guessed}
    return "".join(c if c.lower() in guessed_lower else "_" for c in word)


def is_solved(word: str, guessed: set[str]) -> bool:
    """단어의 모든 글자를 맞혔는지 확인한다."""
    guessed_lower = {g.lower() for g in guessed}
    return set(word.lower()).issubset(guessed_lower)


def play() -> None:
    """한 판을 진행하고 끝나면 메인 메뉴로 돌아간다."""
    word = random.choice(WORDS)
    guessed: set[str] = set()
    attempts_left = 6

    print(f"\n[{GAME_NAME} 게임 시작]")

    while attempts_left > 0:
        masked = mask_word(word, guessed)
        print(f"\n단어: {' '.join(masked)}")
        print(f"남은 기회: {attempts_left}")
        if guessed:
            print(f"시도한 글자: {', '.join(sorted(guessed))}")

        guess = input("한 글자를 추측하세요: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("알파벳 한 글자만 입력하세요.")
            continue

        if guess in guessed:
            print("이미 시도한 글자입니다.")
            continue

        guessed.add(guess)

        if guess in word.lower():
            print(f"맞았습니다! '{guess}'가 포함되어 있습니다.")
            if is_solved(word, guessed):
                print(f"\n정답입니다! 단어: {word}")
                print("축하합니다! 승리하셨습니다.")
                return
        else:
            attempts_left -= 1
            print(f"틀렸습니다! '{guess}'는 포함되어 있지 않습니다.")

    print("\n아쉽습니다. 모든 기회를 소진했습니다.")
    print(f"정답은 '{word}'였습니다.")
