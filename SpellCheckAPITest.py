import requests
import json

url = "https://rapidapi.p.rapidapi.com/api/spelling/SpellCheck"


headers = {
    'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
    'x-rapidapi-key': "4EFkAKPf2zmsh3BXV8O0UCRgymEap1P1EmAjsnuxFXkAqUJ6xT"
    }

text = "teylor swiift"

querystring = {"text": text}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
