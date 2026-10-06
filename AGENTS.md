# AGENTS.md

이 저장소에서 작업하는 코딩 에이전트가 따라야 할 공통 지침입니다.

## 1. 프로젝트 목적

- 창의적공학설계(AD) GitHub 협업 실습용 Python 콘솔 미니 게임 허브입니다.
- 핵심 학습 흐름은 **브랜치 → 커밋 → Pull Request → 코드 리뷰 → 충돌 해결 → 병합**입니다.
- 게임 구현만큼 Git/GitHub 협업 과정과 기록을 중요하게 다룹니다.

## 2. 개발 환경

- Python 3.10 이상
- 의존성은 `requirements.txt`로 관리합니다.
- 기본 검사 도구:
  - `black .`
  - `flake8 .`
  - `pytest`
- 실제 실행 확인:
  - `python main.py`

## 3. 브랜치와 Git 작업 규칙

- `main` 브랜치에 직접 push하지 않습니다.
- 작업 시작 전 항상 최신 `main`을 받습니다.

```bash
git switch main
git pull
```

- 작업은 기능 브랜치에서 진행합니다.
- 게임 브랜치는 `feature/<게임이름>` 형식을 사용합니다.
  - 예: `feature/hangman`, `feature/baseball`, `feature/rps`, `feature/tictactoe`
- 팀장/허브 작업은 `feature/hub`를 사용합니다.
- 현재 브랜치를 확인한 뒤 작업합니다.

```bash
git branch
```

## 4. 담당 범위

| 역할 | 브랜치 | 주 담당 파일 |
|---|---|---|
| A | `feature/hub` | `main.py`, `utils.py`, `README.md` |
| B | `feature/hangman` | `games/hangman.py`, `tests/test_hangman.py` |
| C | `feature/baseball` | `games/baseball.py`, `tests/test_baseball.py` |
| D | `feature/rps` | `games/rps.py`, `tests/test_rps.py` |
| E | `feature/tictactoe` | `games/tictactoe.py`, `tests/test_tictactoe.py` |

- `main.py`와 `README.md`는 여러 팀원이 함께 수정하는 공용 파일이며 충돌 실습 지점입니다.
- 담당 파일 밖의 공용 파일을 수정해야 하면 이유를 명확히 남깁니다.
- 다른 팀원이 사용하는 함수의 이름이나 인자(시그니처)를 임의로 변경하지 않습니다.
- 새 라이브러리를 설치하면 `requirements.txt`를 갱신합니다.

## 5. 구현과 테스트

- 각 게임의 파일 상단 docstring에 적힌 규칙과 함수 힌트를 우선 따릅니다.
- 테스트하기 쉬운 순수 함수로 로직을 분리합니다.
- 잘못된 입력에서도 프로그램이 비정상 종료되지 않도록 합니다.
- 본인 게임의 테스트를 `tests/test_<게임>.py`에 작성합니다.
- 커밋/PR 전에 다음을 확인합니다.

```bash
python main.py
black .
flake8 .
pytest
git status
```

- `venv/`, `.env`, 캐시 파일 등이 스테이징되지 않았는지 확인합니다.

## 6. 커밋 규칙

- 커밋은 가능한 한 작은 의미 단위로 나눕니다.
- 메시지는 변경 목적을 알 수 있게 작성합니다.
- 다음 접두사를 사용합니다.
  - `feat:` 기능
  - `fix:` 버그 수정
  - `test:` 테스트
  - `docs:` 문서
  - `chore:` 기타 작업

예:

```text
feat: 행맨 글자 마스킹 함수 추가
test: 행맨 승리 조건 테스트 추가
docs: README에 행맨 등록
```

## 7. Pull Request와 리뷰

- 기능 브랜치를 push한 뒤 `main`을 대상으로 Pull Request를 생성합니다.
- PR 템플릿의 확인 항목을 채웁니다.
- PR은 **다른 팀원 1명 이상의 승인**을 받은 뒤 병합합니다.
- 본인 PR을 본인이 승인·병합하는 방식으로 리뷰 절차를 우회하지 않습니다.
- 리뷰할 때는 가능하면 브랜치를 직접 받아 실행합니다.

```bash
git fetch
git switch <브랜치>
```

리뷰 시 확인:
- 게임 규칙대로 동작하는가
- 잘못된 입력에서 죽지 않는가
- 함수/변수 이름이 의미 있는가
- 테스트가 존재하고 통과하는가
- 담당 범위 밖 변경에 이유가 있는가
- 비밀 정보나 불필요한 파일이 포함되지 않았는가

## 8. 충돌 해결

PR 병합 순서에 따라 `main.py`와 `README.md` 등에 충돌이 발생할 수 있습니다.

```bash
git switch main
git pull
git switch <내 브랜치>
git merge main
```

- 충돌 구간을 직접 확인하고 필요한 내용을 보존합니다.
- `<<<<<<<`, `=======`, `>>>>>>>` 표시를 남기지 않습니다.
- 해결 후 다시 실행/테스트합니다.

```bash
python main.py
pytest
git add <해결한 파일>
git commit
git push
```

- 병합을 포기하고 이전 상태로 돌아가야 하면 `git merge --abort`를 사용합니다.

## 9. 금지 사항

- `git push --force` 사용 금지
- 비밀번호, API 키, 토큰, `.env` 커밋 금지
- `venv/`, `__pycache__/` 등 불필요한 생성물 커밋 금지
- 충돌 표시가 남은 상태로 커밋 금지
- 리뷰 없이 본인 PR을 직접 승인·병합하는 행위 금지

## 10. 작업 완료 기준

작업 완료 전 최소한 다음 상태여야 합니다.

- 담당 기능이 실행됨
- 관련 테스트가 존재하고 통과함
- `flake8 .` 통과
- 불필요/비밀 파일이 없음
- 의미 있는 작은 커밋으로 기록됨
- PR 설명과 체크리스트가 작성됨
- 다른 팀원의 리뷰를 받을 준비가 됨
