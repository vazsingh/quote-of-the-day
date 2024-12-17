import requests
import json

def get_quote_of_the_day():
    """Fetches a quote of the day from an API."""
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    data = json.loads(response.text)
    quote = data['content']
    author = data['author']
    return f'"{quote}" - {author}'

if __name__ == "__main__":
    quote = get_quote_of_the_day()
    print(quote)
