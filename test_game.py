from collections import namedtuple
from play import EyeGamePage
import pytest


Level = namedtuple("Level", ['name', 'value'])

ROBOT = Level(name='ROBOT', value=30)
JASTRZAB = Level(name='jastrząb', value=25)


@pytest.mark.parametrize("level", [ROBOT])
def test_lvl(driver, level):
    eye_game = EyeGamePage(driver)
    eye_game.load()
    eye_game.get_to_lvl(level=level)
    eye_game.check_lvl_reached(level=level)


@pytest.mark.smoke_test
def test_title(driver):
    eye_game = EyeGamePage(driver)
    eye_game.load()
    assert "Eye" in eye_game.get_title()
