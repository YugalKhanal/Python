from bs4 import BeautifulSoup
import requests
from pathlib import Path

# response = requests.get("https://stackoverflow.com/questions?tab=newest&page=5")
# soup = BeautifulSoup(response.text, "html.parser")
#
# questions = soup.select(".s-post-summary")

path = Path("result.txt")
for i in range(1,11):
    print(f"page {i}")

    response = requests.get(f"https://stackoverflow.com/questions?tab=newest&page={i}")
    soup = BeautifulSoup(response.text, "html.parser")
    questions = soup.select(".s-post-summary")

    for question in questions:
        title = (question.select_one(".s-link").getText())
        print(question.select_one(".s-link").getText())
        vote_count = (question.select_one(".s-post-summary--stats-item-number").getText())
        print(question.select_one(".s-post-summary--stats-item-number").getText())
        with path.open("a") as file:
            file.write(title + "\n")
            file.write(vote_count + "\n")

