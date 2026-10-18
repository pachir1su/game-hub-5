"""네 게임이 허브 메뉴에 연결됐는지 확인합니다."""

from pathlib import Path
import subprocess
import sys

import main


def test_all_four_games_registered():
    assert set(main.GAMES) == {"1", "2", "3", "4"}
    assert {game.GAME_NAME for game in main.GAMES.values()} == {
        "행맨",
        "숫자 야구",
        "가위바위보",
        "틱택토",
    }


def test_show_menu_lists_all_games(capsys):
    main.show_menu()
    output = capsys.readouterr().out

    for number, game in main.GAMES.items():
        assert f"{number}. {game.GAME_NAME}" in output

    assert "0. 종료" in output


def test_menu_routes_all_games_and_exits(monkeypatch, capsys):
    choices = iter(["1", "2", "3", "4", "0"])
    called = []

    def choose(prompt, valid_choices):
        assert valid_choices == {"0", "1", "2", "3", "4"}
        return next(choices)

    monkeypatch.setattr(main, "ask_choice", choose)

    for number, game in main.GAMES.items():
        monkeypatch.setattr(
            game, "play", lambda selected=number: called.append(selected)
        )

    main.main()

    assert called == ["1", "2", "3", "4"]
    assert "안녕히 가세요!" in capsys.readouterr().out


def test_cli_starts_and_exits():
    """실제 Python 프로세스로 허브를 실행한 뒤 종료한다."""
    project_root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [sys.executable, str(project_root / "main.py")],
        input="0\n",
        text=True,
        capture_output=True,
        check=True,
        timeout=10,
    )

    assert "===== Game Hub =====" in result.stdout
    assert "안녕히 가세요!" in result.stdout
