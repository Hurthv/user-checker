from common.utils import get_data
from config import filepath
import requests

data = get_data(filepath)

nick = input("Enter your nickname: ").strip()

for item in data:
    link = item["link"]
    name = item["name"]
    user_link = f"{link}/{nick}"

    response = requests.get(user_link)
    if response.status_code == 200:
        print(f"User found! User link: {user_link}, site name: {name}")
    else:
        print("User not found!")


