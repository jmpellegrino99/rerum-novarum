from bs4 import BeautifulSoup
import requests
import re

# Replace with the website URL you want to scrape
url = "https://www.rockpapershotgun.com/wordle-past-answers"

# Make a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
  # Parse the HTML content
  soup = BeautifulSoup(response.content, "html.parser")

  # Find all <li> elements
  all_li = soup.find_all("li")

  # Filter for 5-letter elements
  five_letter_li = [li for li in all_li if li.text.strip().isupper() and len(li.text.strip()) == 5 and re.match(r"[A-Z]{5}", li.text.strip())]

  past_answers = []

  # Print the text of the filtered elements
  for li in five_letter_li:
    past_answers.append(li.text.strip())
else:
  print("Error: Could not access the website.")

class Words():
  current_words = past_answers