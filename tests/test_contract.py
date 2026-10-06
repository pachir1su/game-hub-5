"""모든 게임 모듈이 공통 계약을 지키는지 확인한다."""

import importlib
import pkgutil

import games


def iter_game_modules():
    for info in pkgutil.iter_modules(games.__path__):
        yield importlib.import_module(f"games.{info.name}")


def test_each_game_follows_contract():
    for module in iter_game_modules():
        assert isinstance(module.GAME_NAME, str) and module.GAME_NAME
        assert callable(module.play)
