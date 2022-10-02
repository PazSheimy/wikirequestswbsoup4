# import required modules
import re
from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError
import sys

# get URL
for urlgiven in sys.argv[1:]:
    url = f"https://en.wikipedia.org/wiki/{urlgiven}_(disambiguation)"

    try:
        response = requests.get(url)
        response.raise_for_status()

    except HTTPError as httperr:
        print(f"Http error: {httperr}")
        sys.exit(1)
    except Exception as err:
        print(f"Someting went really wrong!: {err}")
        sys.exit(1)

    print(response.status_code)
    soup = BeautifulSoup(response.text, "html.parser")
    print(f"{urlgiven}")


    for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
        print(link.get('href'))
