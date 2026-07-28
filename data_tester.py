from common.utils import get_data
from config import filepath
from constructors.req_class import RequestClass
import httpx
import asyncio

data = get_data(filepath)

async def check_single_link(client: RequestClass, item: dict):
    link = item['link']
    try:
        response = await client.get_response(link)

        if response.status_code == 200:
            print(f"Connection to the {link} website was successful")
        else:
            print(f"Unable to connect to the {link} site (Status: {response.status_code})")
    except httpx.TimeoutException:
        print(f"Unable to connect to the {link} site. Error: Timeout")
    except Exception as e:
        print(f"Unable to connect to the {link} site. Error: {e}")

async def test_link(data: list):
    client = RequestClass()

    try:
        tasks = [check_single_link(client, item) for item in data]
        await asyncio.gather(*tasks)
    finally:
        await client.close()

    print("The check was successful!")

# asyncio.run(test_link(data))