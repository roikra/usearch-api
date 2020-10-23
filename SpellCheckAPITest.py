import requests

URL = "https://rapidapi.p.rapidapi.com/api/spelling/SpellCheck"
HEADERS = {
    'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
    'x-rapidapi-key': "Your-X-RapidAPI-Key"
}

text = "teylor swiift"
querystring = {"text": text}

response = requests.get(URL, headers=HEADERS, params=querystring)
print(response.text)
