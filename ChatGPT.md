# ChatGPT.md

이 저장소에서 작업할 때 먼저 `AGENTS.md`를 읽고 그 지침을 따르세요.

## 핵심 규칙

- `main`에 직접 push하지 않습니다.
- 작업 전 `git switch main` → `git pull`로 최신화합니다.
- 게임 작업은 `feature/<게임이름>`, 허브 작업은 `feature/hub`에서 진행합니다.
- 담당 파일 범위를 지키고 공용 파일 수정 이유를 명확히 남깁니다.
- 다른 팀원이 사용하는 함수 이름/인자를 임의로 바꾸지 않습니다.
- 새 라이브러리를 추가하면 `requirements.txt`를 갱신합니다.
- 커밋은 작게 나누고 `feat:`, `fix:`, `test:`, `docs:`, `chore:` 접두사를 사용합니다.
- PR 전 `python main.py`, `black .`, `flake8 .`, `pytest`를 확인합니다.
- PR은 다른 팀원 1명 이상의 리뷰/승인 후 병합합니다.
- 본인 PR의 리뷰 절차를 우회하지 않습니다.
- 충돌 표시는 모두 제거하고 재테스트합니다.
- `git push --force`, 비밀키/토큰/`.env`, `venv/`, `__pycache__/` 커밋은 금지합니다.

세부 역할, 테스트, 리뷰, 충돌 해결 절차는 `AGENTS.md`를 기준으로 합니다.
