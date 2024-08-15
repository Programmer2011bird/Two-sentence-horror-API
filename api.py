from scraping import scraper
from fastapi import FastAPI


SERVER: FastAPI = FastAPI() 


@SERVER.get("/")
def Home(content_type: str = "hot", tops_date: str = "today") -> list[dict[str, str]]:
    SCRAPER: scraper = scraper(content_type, tops_date)
    INFO: list[dict[str, str]] = SCRAPER.get_info()
 
    return INFO
 