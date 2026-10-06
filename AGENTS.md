# AGENTS.md

이 저장소에서 작업하는 모든 코딩 에이전트의 공통 지침입니다.

## 프로젝트 목적

창의적공학설계(AD) 01분반 5조의 GitHub 협업 실습 프로젝트입니다.

강의자료에서 요구하는 핵심 흐름은 다음과 같습니다.

```text
브랜치 → 커밋 → Pull Request → 코드 리뷰 → 충돌 해결 → 병합
```

결과물은 콘솔 미니 게임 4종(행맨, 숫자 야구, 가위바위보, 틱택토)을 하나의 Game Hub 메뉴로 묶는 것입니다.

## 4인 팀 역할

강의자료의 A~E 5인 역할표를 4인 팀에 맞게 조정하여 **A가 E(틱택토) 역할을 겸임**합니다.

| 역할 | GitHub ID | 브랜치 | 담당 |
|---|---|---|---|
| A (팀장) | pachir1su | `feature/hub`, `feature/tictactoe` | 허브/저장소 관리 + 틱택토 |
| B | 팀원 2 | `feature/hangman` | 행맨 |
| C | 팀원 3 | `feature/baseball` | 숫자 야구 |
| D | 팀원 4 | `feature/rps` | 가위바위보 |

세부 파일은 README 역할표를 따릅니다.

## 브랜치 규칙

강의자료의 브랜치 이름을 그대로 사용합니다.

- `feature/hub`
- `feature/hangman`
- `feature/baseball`
- `feature/rps`
- `feature/tictactoe`

`main`에는 직접 push하지 않습니다.

작업 시작 전:

```bash
git switch main
git pull
git switch -c feature/<담당>
git branch
```

이미 브랜치가 있으면 `git switch <브랜치>`로 이동합니다.

## 담당 파일

- A / hub: `main.py`, `utils.py`, `README.md`
- A / tictactoe: `games/tictactoe.py`, `tests/test_tictactoe.py`
- B: `games/hangman.py`, `tests/test_hangman.py`
- C: `games/baseball.py`, `tests/test_baseball.py`
- D: `games/rps.py`, `tests/test_rps.py`

공용 파일을 수정할 때는 이유를 PR에 남깁니다.

다른 팀원이 사용하는 함수의 이름/인자를 바꾸기 전에 협의합니다.

## 구현/테스트

각 게임 파일 상단 docstring의 규칙과 함수 힌트를 우선 따릅니다.

각 게임은 테스트 가능한 순수 함수로 로직을 분리하고 해당 테스트를 작성합니다.

커밋 전 확인:

```bash
python main.py
black .
flake8 .
pytest
git status
```

## 커밋

작은 의미 단위로 커밋합니다.

- `feat:` 기능
- `fix:` 버그
- `test:` 테스트
- `docs:` 문서
- `chore:` 기타

예:

```text
feat: 행맨 글자 마스킹 함수 추가
test: 행맨 승리 조건 테스트 추가
docs: README에 행맨 등록
```

## Pull Request / 리뷰

4인 팀 순환 리뷰:

- A 작성 → B 리뷰
- B 작성 → C 리뷰
- C 작성 → D 리뷰
- D 작성 → A 리뷰

PR은 다른 팀원 1명 이상의 승인 후 병합합니다.

리뷰 시 확인:

- 코드를 직접 내려받아 실행했는가
- 게임 규칙대로 동작하는가
- 잘못된 입력에서도 죽지 않는가
- 함수/변수 이름이 의미 있는가
- 테스트가 있고 통과하는가
- 담당 파일 외 변경에 이유가 있는가
- 비밀키/개인정보/venv 등이 섞이지 않았는가

## 충돌 해결

```bash
git switch main
git pull
git switch <내 브랜치>
git merge main
```

VS Code Merge Editor에서 해결한 뒤:

```bash
python main.py
pytest
git add <해결한 파일>
git commit
git push
```

충돌 표시 `<<<<<<<`, `=======`, `>>>>>>>`를 남기지 않습니다.

잘못되면:

```bash
git merge --abort
```

## 금지

- `git push --force`
- 비밀번호/API Key/토큰/`.env` 커밋
- `venv/`, `__pycache__/` 커밋
- 충돌 표시를 남긴 채 커밋
- 리뷰 없이 본인 PR을 본인이 승인/병합하여 절차 우회

## 완료 기준

- 담당 게임/기능이 동작함
- 테스트 존재 및 통과
- `flake8 .` 통과
- 불필요/비밀 파일 없음
- 작은 의미 단위 커밋
- PR 템플릿 작성
- 지정 리뷰어에게 리뷰 요청
