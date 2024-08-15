from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
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
        
    def get_info(self):
        while True:
            posts: list[WebElement] = self.DRIVER.find_elements(By.TAG_NAME, "shreddit-post")
            
            self.LAST_HEIGHT = self.DRIVER.execute_script("return document.body.scrollHeight;")
            self.DRIVER.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            time.sleep(2.5)

            self.NEW_HEIGHT = self.DRIVER.execute_script("return document.body.scrollHeight;")
            
            if self.NEW_HEIGHT >= 13625:
                print("maximum scroll height reached or exceeded")
                break

            if self.NEW_HEIGHT == self.LAST_HEIGHT:
                break

            for _, post in enumerate(posts):
                self.RAW_INFO: list[str] = post.text.split("\n")
                
                if self.RAW_INFO[4] == "SPOILER":
                    pass

                else:
                    self.POST_INFO: dict[str, str] = {
                        "Author" : self.RAW_INFO[1],
                        "First_Sentence" : self.RAW_INFO[4],
                        "Second_Sentence" : self.RAW_INFO[5],
                        "Number_of_Upvotes" : self.RAW_INFO[7],
                        "Number_of_Comments" : self.RAW_INFO[9]
                    }

                print(self.POST_INFO)
                
                print("----------------------------------------------------------------------------")


if __name__ == "__main__":
    SCRAPER: scraper = scraper()
    SCRAPER.get_info()
