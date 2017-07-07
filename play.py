from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from collections import namedtuple

Level = namedtuple("Level", ['name', 'value'])

class EyeGamePage:

    url = "https://www.igame.com/eye-test/"

    ROBOT = Level(name='robot', value=30)
    JASTRZAB = Level(name='jastrzab', value=25)
    TYGRYS = Level(name='tygrys', value=20)
    KOT = Level(name='kot', value=15)
    PIES = Level(name='pies', value=10)
    KOT = Level(name='kot', value=5)
    NIETOPERZ = Level(name='nietoperz', value=1)

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def load(self):
        self.driver.get(self.url)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))

    def click_chosenone(self):
        self.driver.find_element_by_css_selector(".thechosenone").click()

    def get_to_robot(self):
        for i in range(31):
            self.click_chosenone()
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.ID, "timeleft")))

    def get_to_lvl(self, level):
        for i in range(level.value):
            self.click_chosenone()
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.ID, "timeleft")))

    def set_current_time(self):
        return self.driver.find_element_by_css_selector(".clock").text

    def get_title(self):
        return self.driver.title

    def get_reached_lvl(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.character-title').text

    def check_lvl_reached(self, level):
        assert self.driver.find_element(By.CSS_SELECTOR, '.character-title').text == level.name

    def check_robot_lvl_reached(self):
        self.check_lvl_reached(self.ROBOT)