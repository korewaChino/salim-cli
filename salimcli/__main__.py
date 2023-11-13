
import random
import requests
import json
endpoint = "https://watasalim.vercel.app/api/quotes"



def request() -> dict:
    response = requests.get(endpoint)
    data = response.json()
    return data


def random_quote() -> str:
    data: list(dict) = request()["quotes"]

    # get random entry in list
    quote = data[random.randint(0, len(data) - 1)]

    return quote.get("body")



def main():
    quote = random_quote()

    print(quote)


if __name__ == "__main__":
    main()