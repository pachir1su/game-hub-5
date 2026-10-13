"""숫자 야구 — 담당: C

규칙
- 서로 다른 숫자 3개를 정한다.
- 숫자와 자리 모두 같으면 스트라이크.
- 숫자만 같고 자리가 다르면 볼.
- 최대 9번 추측한다.
"""

import random

GAME_NAME = "숫자 야구"
MAX_TRIES = 9


def make_answer() -> str:
    """중복되지 않는 숫자 3개로 정답을 생성한다."""
    return "".join(random.sample("0123456789", 3))


def judge(answer: str, guess: str) -> tuple[int, int]:
    """정답과 추측을 비교하여 스트라이크와 볼을 반환한다."""
    strikes = 0
    balls = 0

    for i in range(3):
        if guess[i] == answer[i]:
            strikes += 1
        elif guess[i] in answer:
            balls += 1

    return strikes, balls


def valid_guess(guess: str) -> bool:
    """입력한 값이 올바른 세 자리 숫자인지 확인한다."""
    if len(guess) != 3:
        return False

    if not guess.isascii() or not guess.isdigit():
        return False

    if len(set(guess)) != 3:
        return False

    return True


def play() -> None:
    """숫자 야구 게임을 실행한다."""
    answer = make_answer()
    tries = 0

    print(f"\n===== {GAME_NAME} =====")
    print("서로 다른 숫자 3개를 맞혀 보세요!")
    print(f"기회는 총 {MAX_TRIES}번입니다.")
    print("0으로 시작하는 숫자도 가능합니다.\n")

    while tries < MAX_TRIES:
        guess = input(f"[{tries + 1}/{MAX_TRIES}] 숫자 3개 입력: ").strip()

        if not valid_guess(guess):
            print("잘못된 입력입니다.")
            print("중복되지 않는 숫자 3개를 입력하세요.\n")
            continue

        tries += 1
        strikes, balls = judge(answer, guess)

        if strikes == 3:
            print(f"\n정답입니다! {tries}번 만에 맞혔습니다!")
            break

        if strikes == 0 and balls == 0:
            print("아웃! (0 스트라이크, 0 볼)\n")
        else:
            print(f"{strikes} 스트라이크, {balls} 볼\n")

        print(f"남은 기회: {MAX_TRIES - tries}번\n")

    else:
        print("아쉽게도 모든 기회를 사용했습니다.")
        print(f"정답은 {answer}입니다.")

    print("숫자 야구 게임을 종료합니다.\n")
    return


if __name__ == "__main__":
    play()
