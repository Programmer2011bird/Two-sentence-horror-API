from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
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
        posts = self.DRIVER.find_elements(By.TAG_NAME, "shreddit-post")
        
        self.DRIVER.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2.5)

        for index, post in enumerate(posts):
            self.RAW_INFO = post.text.split("\n")
            
            self.POST_INFO = {
                "Author" : self.RAW_INFO[1],
                "First_Sentence" : self.RAW_INFO[4],
                "Second_Sentence" : self.RAW_INFO[5],
                "Number_of_Upvotes" : self.RAW_INFO[7],
                "Number_of_Comments" : self.RAW_INFO[9]
            }

            print(self.POST_INFO)
            
            print("----------------------------------------------------------------------------")


if __name__ == "__main__":
    SCRAPER = scraper()
