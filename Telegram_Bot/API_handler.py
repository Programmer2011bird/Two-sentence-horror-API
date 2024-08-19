from colorama import Fore
import requests


class API_controller:
    def __init__(self) -> None:
        self.URL = "http://127.0.0.1:8000/?content_type=new"

        self.RESPONSE = requests.get(self.URL)
        self.RESPONSE_JSON: list[dict[str, str]] = self.RESPONSE.json()

        for index, self.POST in enumerate(self.RESPONSE_JSON):
            self.AUTHOR = self.POST.get("Author", None)
            self.FIRST_SENTENCE = self.POST.get("First_Sentence", None)
            self.SECOND_SENTENCE = self.POST.get("Second_Sentence", None)
            self.NUMBER_OF_UPVOTES = self.POST.get("Number_of_Upvotes", None)
            self.NUMBER_OF_COMMENTS = self.POST.get("Number_of_Comments", None)

            print(f'{Fore.MAGENTA} ---------------------------{index}---------------------------')
            print(f"{Fore.LIGHTGREEN_EX}AUTHOR : {Fore.CYAN}{self.AUTHOR}")
            print(f"{Fore.LIGHTGREEN_EX}FIRST SENTENCE : {Fore.CYAN}{self.FIRST_SENTENCE}")
            print(f"{Fore.LIGHTGREEN_EX}SECOND SENTENCE : {Fore.CYAN}{self.SECOND_SENTENCE}")
            print(f"{Fore.LIGHTGREEN_EX}NUMBER OF UPVOTES : {Fore.CYAN}{self.NUMBER_OF_UPVOTES}")
            print(f"{Fore.LIGHTGREEN_EX}NUMBER OF COMMENTS : {Fore.CYAN}{self.NUMBER_OF_COMMENTS}")


if __name__ == "__main__":
    API = API_controller()
