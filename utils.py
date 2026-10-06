"""공용 입력 도우미 — 담당: A(팀장)

다른 팀원이 사용하는 함수의 이름/인자를 바꾸기 전에는 반드시 협의합니다.
"""


def ask_int(prompt: str, low: int, high: int) -> int:
    """low 이상 high 이하의 정수가 입력될 때까지 반복해서 묻는다."""
    while True:
        raw = input(prompt).strip()
        if raw.lstrip("-").isdigit() and low <= int(raw) <= high:
            return int(raw)
        print(f"{low}~{high} 사이의 숫자를 입력하세요.")


def ask_yes_no(prompt: str) -> bool:
    """y/n 입력을 받아 True/False를 반환한다."""
    while True:
        raw = input(prompt + " (y/n): ").strip().lower()
        if raw in ("y", "yes"):
            return True
        if raw in ("n", "no"):
            return False
        print("y 또는 n으로 입력하세요.")
