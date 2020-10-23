import requests

URL = "https://rapidapi.p.rapidapi.com/api/spelling/AutoComplete"
HEADERS = {
    "x-rapidapi-host": "contextualwebsearch-websearch-v1.p.rapidapi.com",
    "x-rapidapi-key": "Your-X-RapidAPI-Key"
}
text = "tay"

querystring = {"text": text}

response = requests.get(URL, headers=HEADERS, params=querystring)
print(response.json())
