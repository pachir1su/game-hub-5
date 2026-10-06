"""Game Hub 메인 진입점 — 담당: A(팀장)"""

# [충돌 실습 지점 1] 각 담당자는 자기 게임 import 줄의 주석을 해제합니다.
# from games import hangman
# from games import baseball
# from games import rps
# from games import tictactoe

# [충돌 실습 지점 2] 각 담당자는 자기 메뉴 줄의 주석을 해제합니다.
GAMES = {
    # "1": hangman,
    # "2": baseball,
    # "3": rps,
    # "4": tictactoe,
}


def show_menu() -> None:
    print("\n===== Game Hub =====")
    for key, game in GAMES.items():
        print(f"{key}. {game.GAME_NAME}")
    print("0. 종료")


def main() -> None:
    while True:
        show_menu()
        choice = input("번호를 선택하세요: ").strip()
        if choice == "0":
            print("안녕히 가세요!")
            break

        game = GAMES.get(choice)
        if game is None:
            print("올바른 번호가 아닙니다.")
            continue

        game.play()


if __name__ == "__main__":
    main()
