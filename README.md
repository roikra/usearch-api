# Using Python to call the Search APIs:
  - ##### Web Search API
  - #####  News API
  - ##### Image API
  - #####  Autosuggest API
  - #####  SpellCheck API
  
## Working Code Examples in Python
## Web Search API
```sh
import requests #install from: http://docs.python-requests.org/en/master/

#Replace the following string value with your valid X-RapidAPI-Key.
&Your_X_RapidAPI_Key = "XXXXXXXXXXXXXXXXXXX";

#The query parameters: (update according to your search query)
q = "Taylor%20Swift" #the search query
pageNumber = 1 #the number of requested page
pageSize = 10 #the size of a page
autoCorrect = True #autoCorrectspelling
safeSearch = False #filter results for adult content

response=requests.get("https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/WebSearchAPI?q={}&pageNumber={}&amp;pageSize={}&amp;autocorrect={}&amp;safeSearch={}".format(q, pageNumber, pageSize, autoCorrect,safeSearch),
headers={
"X-RapidAPI-Key": Your_X_RapidAPI_Key
}
).json()

#Get the numer of items returned
totalCount = response["totalCount"];

#Get the list of most frequent searches related to the input search query
relatedSearch = response["relatedSearch"]

#Go over each resulting item
for webPage in response["value"]:

#Get the web page metadata
    url = webPage["url"]
    title = webPage["title"]
    description = webPage["description"]
    keywords = webPage["keywords"]
    provider = webPage["provider"]["name"]
    datePublished = webPage["datePublished"]

    #Get the web page image (if exists)
    imageUrl = webPage["image"]["url"]
    imageHeight = webPage["image"]["height"]
    imageWidth = webPage["image"]["width"]
    
    thumbnail = webPage["image"]["thumbnail"]
    thumbnailHeight = webPage["image"]["thumbnailHeight"]
    thumbnailWidth = webPage["image"]["thumbnailWidth"]

    #An example: Output the webpage url, title and published date:
    print("Url: %s. Title: %s. Published Date:%s." % (url, title, datePublished))
```

## News Search API 
```sh
import requests #install from: http://docs.python-requests.org/en/master/

#Replace the following string value with your valid X-RapidAPI-Key.
Your_X_RapidAPI_Key = "XXXXXXXXXXXXXXXXXXX";

#The query parameters: (update according to your search query)
q = "Taylor%20Swift" #the search query
pageNumber = 1 #the number of requested page
pageSize = 10 #the size of a page
autoCorrect = True #autoCorrectspelling
safeSearch = False #filter results for adult content

response=requests.get("https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/NewsSearchAPI?q={}&amp;pageNumber={}&amp;pageSize={}&amp;autocorrect={}&amp;safeSearch={}".format(q, pageNumber, pageSize, autoCorrect,safeSearch),
headers={
"X-RapidAPI-Key": Your_X_RapidAPI_Key
}
).json()

#Get the numer of items returned
totalCount = response["totalCount"];

#Get the list of most frequent searches related to the input search query
relatedSearch = response["relatedSearch"]

#Go over each resulting item
for webPage in response["value"]:

#Get the web page metadata
    url = webPage["url"]
    title = webPage["title"]
    description = webPage["description"]
    keywords = webPage["keywords"]
    provider = webPage["provider"]["name"]
    datePublished = webPage["datePublished"]

    #Get the web page image (if exists)
    imageUrl = webPage["image"]["url"]
    imageHeight = webPage["image"]["height"]
    imageWidth = webPage["image"]["width"]
    
    thumbnail = webPage["image"]["thumbnail"]
    thumbnailHeight = webPage["image"]["thumbnailHeight"]
    thumbnailWidth = webPage["image"]["thumbnailWidth"]

    #An example: Output the webpage url, title and published date:
    print("Url: %s. Title: %s. Published Date:%s." % (url, title, datePublished))
```

## Image Search API ##
```sh
import requests #install from: http://docs.python-requests.org/en/master/

#Replace the following string value with your valid X-RapidAPI-Key.
Your_X_RapidAPI_Key = "XXXXXXXXXXXXXXXXXXX";

#The query parameters: (update according to your search query)
q = "Taylor%20Swift" #the search query
pageNumber = 1 #the number of requested page
pageSize = 10 #the size of a page
autoCorrect = True #autoCorrectspelling
safeSearch = False #filter results for adult content

response=requests.get("https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/ImageSearchAPI?q={}&amp;pageNumber={}&amp;pageSize={}&amp;autocorrect={}&amp;safeSearch={}".format(q, pageNumber, pageSize, autoCorrect,safeSearch),
headers={
"X-RapidAPI-Key": Your_X_RapidAPI_Key
}
).json()

#Get the numer of items returned
totalCount = response["totalCount"];

#Go over each resulting item
for image in response["value"]:

    # Get the image
    imageUrl = webPage["url"]
    imageHeight = webPage["height"]
    imageWidth = webPage["width"]
    
    # Get the image thumbail
    thumbnail = webPage["thumbnail"]
    thumbnailHeight = webPage["thumbnailHeight"]
    thumbnailWidth = webPage["thumbnailWidth"]

    #An example: Output the webpage url, title and published date:
    print("imageUrl: %s. imageHeight: %s. imageWidth: %s." % (imageUrl, imageHeight, imageWidth))
```


## Autosuggest API ##
### Python 3.x
```sh

import requests #install from: http://docs.python-requests.org/en/master/

#Replace the following string value with your valid X-RapidAPI-Key.
Your_X_RapidAPI_Key = "XXXXXXXXXXXXXX";

#The query parameters: Update according to your search query.
q = "tay" #the search query

response=requests.get("https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/spelling/AutoComplete?text={}".format(q),
headers={
"X-RapidAPI-Key": Your_X_RapidAPI_Key
}
).json()
```


## SpellCheck API ##
```sh

import requests #install from: http://docs.python-requests.org/en/master/

#Replace the following string value with your valid X-RapidAPI-Key.
Your_X_RapidAPI_Key = "XXXXXXXXXXXXXX";

#The query parameters: Update according to your search query.
q = "tay" #the search query

response=requests.get("https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/spelling/AutoComplete?text={}".format(q),
headers={
"X-RapidAPI-Key": Your_X_RapidAPI_Key
}
).json()
```


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)



