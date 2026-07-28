from common.utils import get_data
from config import filepath
from constructors.req_class import RequestClass
import httpx
import asyncio

data = get_data(filepath)
nick = input("Enter your nickname: ").strip()

async def check_single_user_link(client: RequestClass, item: dict):
        link = item["link"]
        user_link = f"{link}/{nick}"
        name = item["name"]
        try:
            response = await client.get_response(user_link)

            if response.status_code == 200:
                print(f"User found! User link: {user_link}, site name: {name}")
            else:
                print(f"User not found! User link: {user_link}, site name: {name}")
        except httpx.TimeoutException:
            print(f"Unable to connect to the {user_link} site. Error: Timeout")
        except Exception as e:
            print(f"Unable to connect to the {user_link} site. Error: {e}")

async def get_info(data: list):
    client = RequestClass()

    try:
        tasks = [check_single_user_link(client, item) for item in data]
        await asyncio.gather(*tasks)
    finally:
        await client.close()

    print("Everything has been completed!")

# asyncio.run(get_info(data))

