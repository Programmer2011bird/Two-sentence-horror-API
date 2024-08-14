from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import selenium.webdriver as WB
import time


class scraper:
    def __init__(self) -> None:
        self.URL: str = "https://www.reddit.com/r/TwoSentenceHorror/"

        self.DRIVER: WebDriver = WB.Chrome()
        self.DRIVER.get(self.URL)
        self.DRIVER.maximize_window()

        # time.sleep(555)


if __name__ == "__main__":
    SCRAPER = scraper()
