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