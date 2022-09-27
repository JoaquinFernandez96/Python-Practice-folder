import requests, pandas as pd

skill = "overall"

page_count = (
    requests.get("https://vidyascape.org/api/highscores/pages/" + skill)
    .json()
    .get("Pages")
)
base_url = "https://vidyascape.org/api/highscores/skill/" + skill + "/"
highscores = []

for i in range(1, page_count + 1):
    response = requests.get(base_url + str(i)).json()
    highscores += response

pd.DataFrame.from_dict(highscores).to_csv(
    "vscapehighscores" + skill + ".csv", index=False
)
