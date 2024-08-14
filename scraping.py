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
        
        time.sleep(5)
        
        self.AUTHOR_CONTAINER = self.DRIVER.find_elements(By.XPATH, '//*[@class="flex justify-between text-12 min-h-[32px]  mb-2xs mt-[-4px]"]/span/span/div')
        
        for index, self.AUTHOR_PARENT in enumerate(self.AUTHOR_CONTAINER):
            print(self.AUTHOR_PARENT.text)
        
        # time.sleep(555)


if __name__ == "__main__":
    SCRAPER = scraper()
