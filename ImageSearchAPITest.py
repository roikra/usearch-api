import requests
import json


url = "https://rapidapi.p.rapidapi.com/api/Search/ImageSearchAPI"

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

for image in response["value"]:

    url = image["url"]
    name = image["name"]
    title = image["title"]

    provider = image["provider"]["name"]

    imageUrl = image["url"]
    imageHeight = image["height"]
    imageWidth = image["width"]

    thumbnail = image["thumbnail"]
    thumbnailHeight = image["thumbnailHeight"]
    thumbnailWidth = image["thumbnailWidth"]

    print("Url: %s. Title: %s." % (url, name))