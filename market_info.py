# from dotenv import load_dotenv
from pprint import pprint
import requests
import os

# load_dotenv()

def get_market_info(search_text="Asahi Linux Zoom call 2023"):
    search_request_url = f"https://api.manifold.markets/v0/search-markets?term={search_text}&limit=1"
    # TODO handle case where there is no 0th entry
    market = requests.get(search_request_url).json()[0]
    # my_list = []
    # market = my_list[0]
    # pprint(market)
    market_info_request_url = f"https://api.manifold.markets/v0/market/{market['id']}"
    top_market = requests.get(market_info_request_url).json()
    # pprint(top_market)
    return top_market

# BINARY has a "probability" field
# MULTIPLE_CHOICE has an "answers" field with a list of dicts with "text" and "probability"
# NUMERIC has ???
# PSEUDO_NUMERIC has ???
# BOUNTIED_QUESTION has ???
# POLL has an "options" field with a list of dicts with "text" and "votes"
# STONK has fucking nothing
# maybe go too the URL of the market if it's weird

if __name__ == "__main__":
    print("\n***Get Market Info***\n")
    search_text = input("\nPlease enter your search text: ")
    market_data = get_market_info(search_text)
    print("\n")
    pprint(market_data)
