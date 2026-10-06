"""틱택토 — 담당: A(팀장, 4인 팀에서 E 역할 겸임)

규칙
- 2명이 번갈아 X, O를 3x3 판에 놓는다.
- 가로/세로/대각선 3칸을 먼저 채우면 승리.
- 판이 가득 차면 무승부.
"""

GAME_NAME = "틱택토"
EMPTY = " "


def check_winner(board: list[list[str]]) -> str | None:
    """승자가 있으면 'X' 또는 'O'를 반환하고, 없으면 None을 반환한다."""
    lines = list(board)
    lines.extend([[board[row][col] for row in range(3)] for col in range(3)])
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])

    for line in lines:
        if line[0] != EMPTY and line.count(line[0]) == 3:
            return line[0]
    return None


def is_full(board: list[list[str]]) -> bool:
    """빈 칸이 없으면 True를 반환한다."""
    return all(cell != EMPTY for row in board for cell in row)


def render_board(board: list[list[str]]) -> None:
    """현재 보드를 출력한다."""
    for row_index, row in enumerate(board):
        print(" | ".join(row))
        if row_index < 2:
            print("--+---+--")


def position_to_index(position: int) -> tuple[int, int]:
    """1~9 위치 번호를 (행, 열) 인덱스로 변환한다."""
    return divmod(position - 1, 3)


def ask_position(board: list[list[str]], player: str) -> tuple[int, int]:
    """놓을 수 있는 위치를 입력받을 때까지 반복한다."""
    while True:
        raw = input(f"{player} 차례입니다. 위치를 고르세요 (1~9): ").strip()

        if not raw.isdigit():
            print("1~9 사이 숫자를 입력하세요.")
            continue

        position = int(raw)
        if not 1 <= position <= 9:
            print("1~9 사이 숫자를 입력하세요.")
            continue

        row, col = position_to_index(position)
        if board[row][col] != EMPTY:
            print("이미 선택된 칸입니다.")
            continue

        return row, col


def play() -> None:
    """틱택토 한 판을 진행하고 끝나면 메인 메뉴로 돌아간다."""
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    player = "X"

    print("\n위치 번호")
    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9")
    print()

    while True:
        render_board(board)
        row, col = ask_position(board, player)
        board[row][col] = player

        winner = check_winner(board)
        if winner is not None:
            render_board(board)
            print(f"{winner} 승리!")
            return

        if is_full(board):
            render_board(board)
            print("무승부입니다.")
            return

        player = "O" if player == "X" else "X"
