"""가위바위보 – 담당: D

규칙
- 컴퓨터와 3판 2선승제로 대결한다.
- 입력: 1(가위), 2(바위), 3(보)

구현 힌트
- decide(player: str, computer: str) -> str
  반환값: "win" | "lose" | "draw"
"""

import random

GAME_NAME = "가위바위보"

SCISSORS = "가위"
ROCK = "바위"
PAPER = "보"
CHOICES = (SCISSORS, ROCK, PAPER)

WIN = "win"
LOSE = "lose"
DRAW = "draw"

# 키 선택지가 이기는 상대 선택지
BEATS = {
    SCISSORS: PAPER,
    ROCK: SCISSORS,
    PAPER: ROCK,
}

NUMBER_TO_CHOICE = {"1": SCISSORS, "2": ROCK, "3": PAPER}
WINS_NEEDED = 2
QUIT_WORDS = ("q", "quit", "exit")


def normalize(value):
    """입력을 '가위'/'바위'/'보' 중 하나로 바꾼다.

    1, 2, 3 또는 가위, 바위, 보를 받을 수 있다.
    올바르지 않은 입력이면 None을 반환한다.
    """
    if not isinstance(value, str):
        return None
    value = value.strip()
    if value in NUMBER_TO_CHOICE:
        return NUMBER_TO_CHOICE[value]
    if value in CHOICES:
        return value
    return None


def decide(player: str, computer: str) -> str:
    """플레이어 기준 승패를 "win", "lose", "draw" 중 하나로 반환한다."""
    player_choice = normalize(player)
    computer_choice = normalize(computer)
    if player_choice is None or computer_choice is None:
        raise ValueError("가위, 바위, 보 중 하나여야 합니다.")
    if player_choice == computer_choice:
        return DRAW
    if BEATS[player_choice] == computer_choice:
        return WIN
    return LOSE


def get_computer_choice() -> str:
    """컴퓨터의 선택을 무작위로 정한다."""
    return random.choice(CHOICES)


def is_match_over(player_wins: int, computer_wins: int) -> bool:
    """어느 한쪽이 필요한 승수에 도달했는지 확인한다."""
    return player_wins >= WINS_NEEDED or computer_wins >= WINS_NEEDED


def play() -> None:
    """3판 2선승 한 판을 진행하고 메인 메뉴로 돌아간다."""
    print(f"=== {GAME_NAME} (3판 2선승제) ===")
    print("1: 가위, 2: 바위, 3: 보, q: 메인 메뉴로")

    player_wins = 0
    computer_wins = 0
    round_number = 1

    while not is_match_over(player_wins, computer_wins):
        try:
            text = input(f"[{round_number}라운드] 선택 > ")
        except EOFError:
            print()
            return

        if text.strip().lower() in QUIT_WORDS:
            print("메인 메뉴로 돌아갑니다.")
            return

        player = normalize(text)
        if player is None:
            print("잘못된 입력입니다. 1, 2, 3 중에서 입력하세요.")
            continue

        computer = get_computer_choice()
        result = decide(player, computer)
        print(f"나: {player} / 컴퓨터: {computer}")

        if result == DRAW:
            print("비겼습니다. 다시 합니다.")
            continue

        if result == WIN:
            player_wins += 1
            print("이번 라운드는 내가 이겼습니다!")
        else:
            computer_wins += 1
            print("이번 라운드는 컴퓨터가 이겼습니다.")
        print(f"전적: 나 {player_wins} - 컴퓨터 {computer_wins}")
        round_number += 1

    if player_wins > computer_wins:
        print("최종 승리! 축하합니다!")
    else:
        print("최종 패배... 다음에 다시 도전하세요.")
