# Using Python to call the Search APIs:
  - ##### Web Search API
  - #####  News API
  - ##### Image API
  - #####  Autosuggest API
  - #####  SpellCheck API
  
## Web Search API
```sh
mport requests

URL = "https://rapidapi.p.rapidapi.com/api/Search/WebSearchAPI"
HEADERS = {
    'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
    'x-rapidapi-key': "Your-X-RapidAPI-Key"
}

query = "taylor swift"
page_number = 1
page_size = 10
auto_correct = True
safe_search = False

querystring = {"q": query,
               "pageNumber": page_number,
               "pageSize": page_size,
               "autoCorrect": auto_correct,
               "safeSearch": safe_search}
response = requests.get(URL, headers=HEADERS, params=querystring).json()

print(response)

total_count = response["totalCount"]

for web_page in response["value"]:

    url = web_page["url"]
    title = web_page["title"]
    description = web_page["description"]
    body = web_page["body"]
    date_published = web_page["datePublished"]
    language = web_page["language"]
    is_safe = web_page["isSafe"]
    provider = web_page["provider"]["name"]

    print("Url: {}. Title: {}.".format(url, title))
```

## News Search API
```sh
import requests

URL = "https://rapidapi.p.rapidapi.com/api/search/NewsSearchAPI"
HEADERS = {
    "x-rapidapi-host": "contextualwebsearch-websearch-v1.p.rapidapi.com",
    "x-rapidapi-key": "Your-X-RapidAPI-Key"
}

query = "taylor swift"
page_number = 1
page_size = 10
auto_correct = True
safe_search = False
with_thumbnails = True
to_published_date = ""
from_published_date = ""

querystring = {"q": query,
               "pageNumber": page_number,
               "pageSize": page_size,
               "autoCorrect": auto_correct,
               "safeSearch": safe_search,
               "withThumbnails": with_thumbnails,
               "fromPublishedDate": to_published_date,
               "toPublishedDate": from_published_date}

response = requests.get(URL, headers=HEADERS, params=querystring).json()

print(response)

total_count = response["totalCount"]

for web_page in response["value"]:
    url = web_page["url"]
    title = web_page["title"]
    description = web_page["description"]
    body = web_page["body"]
    date_published = web_page["datePublished"]
    language = web_page["language"]
    is_safe = web_page["isSafe"]
    provider = web_page["provider"]["name"]

    image_url = web_page["image"]["url"]
    image_height = web_page["image"]["height"]
    image_width = web_page["image"]["width"]

    thumbnail = web_page["image"]["thumbnail"]
    thumbnail_height = web_page["image"]["thumbnailHeight"]
    thumbnail_width = web_page["image"]["thumbnailWidth"]

    print("Url: {}. Title: {}. Published Date: {}.".format(url, title, date_published))
```

## Image Search API ##
```sh
import requests

URL = "https://rapidapi.p.rapidapi.com/api/Search/ImageSearchAPI"
HEADERS = {
    'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
    'x-rapidapi-key': "Your-X-RapidAPI-Key"
}

q = "taylor swift"
page_number = 1
page_size = 10
auto_correct = True
safe_search = False

querystring = {"q": q,
               "pageNumber": page_number,
               "pageSize": page_size,
               "autoCorrect": auto_correct,
               "safeSearch": safe_search}

response = requests.get(URL, headers=HEADERS, params=querystring).json()

print(response)

totalCount = response["totalCount"]

for image in response["value"]:

    url = image["url"]
    name = image["name"]
    title = image["title"]

    provider = image["provider"]["name"]

    image_url = image["url"]
    image_height = image["height"]
    imageWidth = image["width"]

    thumbnail = image["thumbnail"]
    thumbnail_height = image["thumbnailHeight"]
    thumbnail_width = image["thumbnailWidth"]

    print("Url: %s. Title: %s." % (url, name))
```

## Autosuggest API ##
```sh
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

```


## SpellCheck API ##
```sh
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
```


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

