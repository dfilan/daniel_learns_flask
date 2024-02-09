# from dotenv import load_dotenv
from pprint import pprint
import requests
import os

# load_dotenv()

def get_market_info(search_text="Asahi Linux Zoom call 2023"):
    search_request_url = f"https://api.manifold.markets/v0/search-markets?term={search_text}&limit=1"
    market_list = requests.get(search_request_url).json()
    if not market_list:
        return None
    else:
        market = market_list[0]
        # pprint(market)
        market_info_request_url = f"https://api.manifold.markets/v0/market/{market['id']}"
        top_market = requests.get(market_info_request_url).json()
        # pprint(top_market)
        return top_market

if __name__ == "__main__":
    print("\n***Get Market Info***\n")
    search_text = input("\nPlease enter your search text: ")
    market_data = get_market_info(search_text)
    print("\n")
    pprint(market_data)
