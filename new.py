import httpx

latitude = 37.7749
longitude = -122.4194
url = f"https://geo.fcc.gov/api/census/block/find?latitude={latitude}&longitude={longitude}&censusYear=2020&format=json"

response = httpx.get(url)

# Check if the request was successful
if response.status_code == 200:
    json_data = response.json()
    print(json_data)
else:
    print(f"Error: {response.status_code}")

