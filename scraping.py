from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from itertools import zip_longest
import selenium.webdriver as WB
import time

class scraper:
    def __init__(self) -> None:
        self.URL: str = "https://www.reddit.com/r/TwoSentenceHorror/"

        self.DRIVER: WebDriver = WB.Chrome()
        self.DRIVER.get(self.URL)
        self.DRIVER.maximize_window()
        
        time.sleep(5)
        
        self.get_info()

    def get_info(self):
        AUTHOR_CONTAINER = self.DRIVER.find_elements(By.XPATH, '//*[@class="flex justify-between text-12 min-h-[32px]  mb-2xs mt-[-4px]"]/span/span/div')
        FIRST_SENTENCE_CONTAINER = self.DRIVER.find_elements(By.XPATH, '//*[@class="block font-semibold text-neutral-content-strong m-0 visited:text-neutral-content-weak text-16 xs:text-18  mb-2xs xs:mb-xs "]')
        SECOND_SENTENCE_CONTAINER = self.DRIVER.find_elements(By.XPATH, '//*[@class="hover:no-underline no-underline pointer-events-none text-neutral-content visited:text-neutral-content-weak"]')
        
        self.AUTHORS: list[str] = []
        self.FIRST_SENTENCES: list[str] = []
        self.SECOND_SENTENCES: list[str] = []

        for index, AUTHOR in enumerate(AUTHOR_CONTAINER):
            self.AUTHORS.append(AUTHOR.text)

        for index, FIRST_SENTENCE in enumerate(FIRST_SENTENCE_CONTAINER):
            self.FIRST_SENTENCES.append(FIRST_SENTENCE.text)
        
        for index, SECOND_SENTENCE in enumerate(SECOND_SENTENCE_CONTAINER):
            self.SECOND_SENTENCES.append(SECOND_SENTENCE.text)

        print(list(zip_longest(self.AUTHORS, self.FIRST_SENTENCES, self.SECOND_SENTENCES, fillvalue=None)))
 

if __name__ == "__main__":
    SCRAPER = scraper()
