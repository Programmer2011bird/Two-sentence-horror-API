from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import selenium.webdriver as WB
from typing import Any
import time


class scraper:
    def __init__(self, content_type: str = "hot", tops_date: str = "today") -> None:
        match content_type.lower():
            case "new":
                self.URL: str = "https://www.reddit.com/r/TwoSentenceHorror/new/"
            
            case "top":
                match tops_date.lower():
                    case "today":
                        self.URL: str= "https://www.reddit.com/r/TwoSentenceHorror/top/?t=day"
                    
                    case "thisweek":
                        self.URL: str = "https://www.reddit.com/r/TwoSentenceHorror/top/?t=week"
                    
                    case "thismonth":
                        self.URL: str = "https://www.reddit.com/r/TwoSentenceHorror/top/?t=month"
                    
                    case "thisyear":
                        self.URL: str = "https://www.reddit.com/r/TwoSentenceHorror/top/?t=year"
                    
                    case "alltime":
                        self.URL: str = "https://www.reddit.com/r/TwoSentenceHorror/top/?t=all"
            
            case "hot":
                self.URL: str = "https://www.reddit.com/r/TwoSentenceHorror/"
        
        time.sleep(5)

        self.DRIVER: WebDriver = WB.Chrome()
        self.DRIVER.get(self.URL)
        self.DRIVER.maximize_window()
        
        time.sleep(5)
        
    def get_info(self) -> list[dict[str, str]]:
        self.POSTS_LIST: list[dict[str, str]] = []

        while True:
            posts: list[WebElement] = self.DRIVER.find_elements(By.TAG_NAME, "shreddit-post")
            
            self.LAST_HEIGHT: Any = self.DRIVER.execute_script("return document.body.scrollHeight;")
            self.DRIVER.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            time.sleep(2.5)

            self.NEW_HEIGHT: Any = self.DRIVER.execute_script("return document.body.scrollHeight;")
            
            if self.NEW_HEIGHT >= 13625:
                print("maximum scroll height reached or exceeded")
                
                return self.POSTS_LIST

                break

            if self.NEW_HEIGHT == self.LAST_HEIGHT:
                return self.POSTS_LIST
            
                break
                
            for _, post in enumerate(posts):
                self.RAW_INFO: list[str] = post.text.split("\n")
                
                if self.RAW_INFO[4] == "SPOILER":
                    pass
                
                if self.RAW_INFO[5] == "Upvote":
                    self.RAW_INFO[5] = None

                else:
                    self.POST_INFO: dict[str, str] = {
                        "Author" : self.RAW_INFO[1],
                        "First_Sentence" : self.RAW_INFO[4],
                        "Second_Sentence" : self.RAW_INFO[5],
                        "Number_of_Upvotes" : self.RAW_INFO[7],
                        "Number_of_Comments" : self.RAW_INFO[9]
                    }

                    self.POSTS_LIST.append(self.POST_INFO)
