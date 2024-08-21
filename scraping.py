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
                self.URL: str = "https://www.reddit.com/r/TwoSentenceHorror/new/?rdt=53161"
            
            case "top":
                match tops_date.lower():
                    case "today":
                        self.URL: str= "https://www.reddit.com/r/TwoSentenceHorror/top/?t=day&rdt=53161"
                    
                    case "thisweek":
                        self.URL: str = "https://www.reddit.com/r/TwoSentenceHorror/top/?t=week&rdt=53161"
                    
                    case "thismonth":
                        self.URL: str = "https://www.reddit.com/r/TwoSentenceHorror/top/?t=month&rdt=53161"
                    
                    case "thisyear":
                        self.URL: str = "https://www.reddit.com/r/TwoSentenceHorror/top/?t=year&rdt=53161"
                    
                    case "alltime":
                        self.URL: str = "https://www.reddit.com/r/TwoSentenceHorror/top/?t=all&rdt=53161"
            
            case "hot":
                self.URL: str = "https://www.reddit.com/r/TwoSentenceHorror/?rdt=53161"
        
        self.DRIVER: WebDriver = WB.Chrome()
        self.DRIVER.get(self.URL)
        self.DRIVER.maximize_window()
        
        time.sleep(2.5)
        
    def get_info(self) -> list[dict[str, str]]:
        self.POSTS_INFO: list[dict[str, str]] = []

        while True:
            self.posts: list[WebElement] = self.DRIVER.find_elements(By.TAG_NAME, "shreddit-post")
            
            self.DRIVER.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            time.sleep(2.5)
            NEW_HEIGHT: Any = self.DRIVER.execute_script("return document.body.scrollHeight;")
            time.sleep(2)

            if NEW_HEIGHT >= 13625:
                print("maximum scroll height reached or exceeded")
                
                return self.POSTS_INFO

                break

            self.enumerate_posts()
    
    def enumerate_posts(self) -> None:
        for _, post in enumerate(self.posts):
            try:
                CONTENT: list[str] = post.text.split('\n')

                if CONTENT[4].lower() == "spoiler":
                    self.FIRST_SENTENCE: str = CONTENT[0]
                    self.SECOND_SENTENCE: str = CONTENT[-7]
                    self.AUTHOR: str = CONTENT[1]
                    self.REDDIT_UPVOTES: str = CONTENT[-4]
                    self.TIME: str = CONTENT[3]
                    self.TYPE: str = "spoiler"
                       
                    self.INFO: dict[str, str] = {
                        "First_Sentence" : self.FIRST_SENTENCE,
                        "Second_Sentence" : self.SECOND_SENTENCE,
                        "Author" : self.AUTHOR,
                        "Reddit_Upvotes" : self.REDDIT_UPVOTES,
                        "Time" : self.TIME,
                        "Type" : self.TYPE
                    }
                        
                    self.POSTS_INFO.append(self.INFO)

                elif CONTENT[4].lower() == "nsfw":
                    self.FIRST_SENTENCE: str= CONTENT[0]
                    self.SECOND_SENTENCE: str = CONTENT[-7]
                    self.AUTHOR: str = CONTENT[1]
                    self.REDDIT_UPVOTES: str = CONTENT[-4]
                    self.TIME: str = CONTENT[3]
                    self.TYPE: str = "nsfw"
                        
                    self.INFO: dict[str, str] = {
                        "First_Sentence" : self.FIRST_SENTENCE,
                        "Second_Sentence" : self.SECOND_SENTENCE,
                        "Author" : self.AUTHOR,
                        "Reddit_Upvotes" : self.REDDIT_UPVOTES,
                        "Time" : self.TIME,
                        "Type" : self.TYPE
                    }
                    self.POSTS_INFO.append(self.INFO)

                else : 
                    self.FIRST_SENTENCE: str = CONTENT[0]
                    self.SECOND_SENTENCE: str = CONTENT[-6]
                    self.AUTHOR: str = CONTENT[1]
                    self.REDDIT_UPVOTES: str = CONTENT[-4]
                    self.TIME: str = CONTENT[3]
                    self.TYPE: str = "normal"
                
                    self.INFO: dict[str, str] = {
                        "First_Sentence" : self.FIRST_SENTENCE,
                        "Second_Sentence" : self.SECOND_SENTENCE,
                        "Author" : self.AUTHOR,
                        "Reddit_Upvotes" : self.REDDIT_UPVOTES,
                        "Time" : self.TIME,
                        "Type" : self.TYPE
                    }
                        
                    self.POSTS_INFO.append(self.INFO)

            except Exception:
                continue
