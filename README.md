# 🎮 Game Hub

창의적공학설계(AD) 01분반 5조 조별과제

4인 팀 GitHub 협업 실습용 Python 콘솔 미니 게임 허브입니다.

> 강의자료의 5인 역할표(A~E)를 4인 팀에 맞게 조정했습니다.  
> **A(팀장)가 E 역할의 틱택토까지 겸임**하고, 나머지 역할/브랜치 이름은 강의자료를 그대로 따릅니다.

## 실행 방법

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
python main.py
```

## 5조 역할 분담

| 역할 | GitHub ID | 담당 브랜치 | 담당 파일 / 업무 |
|---|---|---|---|
| A (팀장) | **pachir1su** | `feature/hub`, `feature/tictactoe` | `main.py`, `utils.py`, `README.md`, 저장소/병합 관리 + `games/tictactoe.py`, `tests/test_tictactoe.py` |
| B | 팀원 2 | `feature/hangman` | `games/hangman.py`, `tests/test_hangman.py` |
| C | 팀원 3 | `feature/baseball` | `games/baseball.py`, `tests/test_baseball.py` |
| D | 팀원 4 | `feature/rps` | `games/rps.py`, `tests/test_rps.py` |

팀원 GitHub ID가 정해지면 `팀원 2~4`를 실제 ID로 교체합니다.

## 4인 팀 순환 리뷰

강의자료의 순환 리뷰 방식을 4인 팀에 맞게 적용합니다.

| PR 작성자 | 리뷰어 |
|---|---|
| A | B |
| B | C |
| C | D |
| D | A |

- 각 PR은 **다른 팀원 1명 이상 승인** 후 병합합니다.
- 본인 PR을 본인이 승인/병합하는 방식으로 리뷰 절차를 우회하지 않습니다.

## 게임 목록

| 번호 | 게임 | 담당 | 브랜치 | 상태 |
|---|---|---|---|---|
| 1 | 행맨 | B | `feature/hangman` | 🚧 |
| 2 | 숫자 야구 | C | `feature/baseball` | 🚧 |
| 3 | 가위바위보 | D | `feature/rps` | 🚧 |
| 4 | 틱택토 | A | `feature/tictactoe` | 🚧 |

## 협업 흐름

```text
main 최신화
  ↓
feature/<작업> 브랜치 생성
  ↓
개발 + 테스트
  ↓
작은 단위 commit
  ↓
push
  ↓
Pull Request
  ↓
다른 팀원 코드 리뷰
  ↓
Approve
  ↓
충돌 해결
  ↓
Merge
```

## Git 규칙

- `main`에 직접 push하지 않습니다.
- 작업 전:
  ```bash
  git switch main
  git pull
  ```
- 브랜치:
  - 팀장/허브: `feature/hub`
  - 행맨: `feature/hangman`
  - 숫자 야구: `feature/baseball`
  - 가위바위보: `feature/rps`
  - 틱택토: `feature/tictactoe`
- 커밋 메시지:
  - `feat:` 기능
  - `fix:` 버그
  - `test:` 테스트
  - `docs:` 문서
  - `chore:` 기타
- 커밋 전:
  ```bash
  black .
  flake8 .
  pytest
  git status
  ```
- `git push --force` 금지
- 비밀번호, 토큰, API Key, `.env`, `venv/`, `__pycache__/` 커밋 금지

## 충돌 해결

```bash
git switch main
git pull
git switch <내 브랜치>
git merge main
```

VS Code Merge Editor에서 충돌을 해결한 뒤:

```bash
python main.py
pytest
git add <해결한 파일>
git commit
git push
```

충돌 해결을 취소하려면:

```bash
git merge --abort
```
