import requests
import pandas as pd

def fetch_and_parse_json_data(url):
    # Send the request to the API
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Parse the JSON response
    json_data = response.json()

    # Initialize a list to store parsed data
    data = []

    # Extract information from the JSON response
    # Assuming the JSON structure has 'Block', 'County', and 'State' fields
    block = json_data.get('Block', {})
    county = json_data.get('County', {})
    state = json_data.get('State', {})

    block_info = {
        'Block FIPS': block.get('FIPS', 'N/A')[:12],
        'Bounding Box': block.get('bbox', 'N/A'),
        'County FIPS': county.get('FIPS', 'N/A'),
        'County Name': county.get('name', 'N/A'),
        'State FIPS': state.get('FIPS', 'N/A'),
        'State Code': state.get('code', 'N/A'),
        'State Name': state.get('name', 'N/A')
    }

    for key in block_info:
        print(block_info[key], type(block_info[key]))

lat = 41.25829
long = -73.13798

# Example API URL
url = f"https://geo.fcc.gov/api/census/block/find?latitude={lat}&longitude={long}&censusYear=2020&format=json"

fetch_and_parse_json_data(url)
