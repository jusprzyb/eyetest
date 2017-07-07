from browser import get_driver
from play import EyeGamePage

def test_kret_lvl():
    driver = get_driver()
    eye_game = EyeGamePage(driver)
    eye_game.load()
    eye_game.get_to_robot()
    eye_game.check_robot_lvl_reached()
