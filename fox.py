import requests
from bs4 import BeautifulSoup
import time

# Define the URL of the website you want to scrape
url = "https://www.foxnews.com/"

time_string = time.ctime()

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the first <h3> element on the page
    first_h3 = soup.find("h3")

    # Check if an <h3> element was found
    if first_h3:
        # Extract and print the text of the <h3> element
        print(f"{time_string}: {first_h3.text}")
    else:
        print(f"{time_string}: No headline found on the page.")
else:
    print("Failed to retrieve the web page. Status code:", response.status_code)
