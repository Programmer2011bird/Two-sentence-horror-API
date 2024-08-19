from colorama import Fore
import requests


class API_controller:
    def __init__(self) -> None:
        self.URL: str = "http://127.0.0.1:8000/?content_type=new"

        self.RESPONSE: requests.Response = requests.get(self.URL)
        self.RESPONSE_JSON: list[dict[str, str]] = self.RESPONSE.json()

    def get_info(self, func) -> None:
        for index, self.POST in enumerate(self.RESPONSE_JSON):
            self.AUTHOR: str | None = self.POST.get("Author", None)
            self.FIRST_SENTENCE: str | None = self.POST.get("First_Sentence", None)
            self.SECOND_SENTENCE: str | None = self.POST.get("Second_Sentence", None)
            self.NUMBER_OF_UPVOTES: str | None = self.POST.get("Number_of_Upvotes", None)
            self.NUMBER_OF_COMMENTS: str | None = self.POST.get("Number_of_Comments", None)

            print(f'{Fore.MAGENTA} ---------------------------{index}---------------------------')
            print(f"{Fore.LIGHTGREEN_EX}AUTHOR : {Fore.CYAN}{self.AUTHOR}")
            print(f"{Fore.LIGHTGREEN_EX}FIRST SENTENCE : {Fore.CYAN}{self.FIRST_SENTENCE}")
            print(f"{Fore.LIGHTGREEN_EX}SECOND SENTENCE : {Fore.CYAN}{self.SECOND_SENTENCE}")
            print(f"{Fore.LIGHTGREEN_EX}NUMBER OF UPVOTES : {Fore.CYAN}{self.NUMBER_OF_UPVOTES}")
            print(f"{Fore.LIGHTGREEN_EX}NUMBER OF COMMENTS : {Fore.CYAN}{self.NUMBER_OF_COMMENTS}")

            func()
