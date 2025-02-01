# API Handling
import requests
from requests.exceptions import RequestException, HTTPError, Timeout


# Fetch random quote
def fetch_random_quote():
    URL = "https://api.freeapi.app/api/v1/public/quotes/quote/random"

    try:
        response_object = requests.get(URL)
        response_object.raise_for_status()

        # Raise HTTP error if any
        response = response_object.json()

        if not response.get("success"):
            raise RequestException("Request failed!")

        data = response.get("data", {})

        quote = data.get("content", "")
        author = data.get("author", "")
        tags = data.get("tags", [])
        return quote, author, tags
    except (RequestException, HTTPError, Timeout, KeyError):
        print(f"Error fetching data!")
        return None, None, None


# Main
def main():
    quote, author, tags = fetch_random_quote()

    if quote and author:
        print(f'\n"{quote}"')
        print(f"- {author}")

        if tags:
            print("\nTags:", ", ".join(tags))
    else:
        print("\nFailed to fetch quote!")


# Initializing program
if __name__ == "__main__":
    main()
