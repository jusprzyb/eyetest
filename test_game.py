from browser import get_driver
from collections import namedtuple
from play import EyeGamePage
import pytest


Level = namedtuple("Level", ['name', 'value'])

ROBOT = Level(name='robot', value=30)
JASTRZAB = Level(name='jastrzab', value=25)

@pytest.mark.parametrize("level", [JASTRZAB, ROBOT])

def test_lvl(driver, lvl):
    eye_game = EyeGamePage(driver)
    eye_game.load()
    eye_game.get_to_lvl(level=lvl)
    eye_game.check_robot_lvl_reached()
