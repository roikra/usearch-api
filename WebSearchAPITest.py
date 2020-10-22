import requests
import json


url = "https://rapidapi.p.rapidapi.com/api/Search/WebSearchAPI"

headers = {
    'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
    'x-rapidapi-key': "4EFkAKPf2zmsh3BXV8O0UCRgymEap1P1EmAjsnuxFXkAqUJ6xT"
    #'x-rapidapi-key': "YOUR_API_KEY"
    }


q = "taylor swift"
pageNumber = 1
pageSize = 10
autoCorrect = True
safeSearch = False

querystring = {"q":q, "pageNumber":pageNumber, "pageSize":pageSize, "autoCorrect":autoCorrect, "safeSearch":safeSearch}
response = json.loads(requests.request("GET", url, headers=headers, params=querystring).text)

print(response)

totalCount = response["totalCount"];

for webPage in response["value"]:

    url = webPage["url"]
    title = webPage["title"]
    description = webPage["description"]
    body = webPage["body"]
    datePublished = webPage["datePublished"]
    language = webPage["language"]
    isSafe = webPage["isSafe"]
    provider = webPage["provider"]["name"]

    print("Url: %s. Title: %s. Published Date:%s." % (url, title, datePublished))