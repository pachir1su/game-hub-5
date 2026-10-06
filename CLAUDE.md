# CLAUDE.md

작업 전 `AGENTS.md`와 `README.md`를 기준으로 진행하세요.

핵심:
- 강의자료 기준 브랜치: `feature/hub`, `feature/hangman`, `feature/baseball`, `feature/rps`, `feature/tictactoe`
- 4인 팀이므로 A가 hub와 tictactoe를 겸임
- `main` 직접 push 금지
- 작업 전 `git switch main` → `git pull`
- 담당 파일과 공용 파일 경계 준수
- 테스트 가능한 함수와 테스트 작성
- 커밋 전 `python main.py`, `black .`, `flake8 .`, `pytest`
- 작은 단위 커밋과 `feat/fix/test/docs/chore` 접두사 사용
- 순환 리뷰 후 병합
- 충돌 해결 후 전체 동작 재확인
- force push/비밀정보/venv/cache 커밋 금지

세부 지침은 `AGENTS.md`가 우선합니다.
