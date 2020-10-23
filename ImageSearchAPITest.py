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