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

GAME_NAME = "행맨"


def play() -> None:
    """한 판을 진행하고 끝나면 메인 메뉴로 돌아간다."""
    print(f"[{GAME_NAME}] 아직 구현되지 않았습니다.")
