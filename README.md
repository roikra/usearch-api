# newsapi-python
A Python client for ContextualWeb news API
# Contextual Web ([contextualwebsearch.com])

## News API. Clients for News API in Python

Billions of news with a single API call. 
The API returns a list of relevant results from a search query.

To generate your RapidAPI key please [subscribe] to one of our proposed plans.

#  Support
24/7 Email Support: support@contextualwebsearch.com

## News API ##
### Python 3.x
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

response=requests.get("https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/NewsSearchAPI?q={}&pageNumber={}&pageSize={}&autocorrect={}&safeSearch={}".format(q, pageNumber, pageSize, autoCorrect,safeSearch),
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

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [subscribe]:  <https://rapidapi.com/contextualwebsearch/api/web-search/pricing>
   [contextualwebsearch.com]: <https://www.contextualwebsearch.com/>
   [Advanced search]: <http://contextualwebsearch.com/advanced_search>
   [Site search]: <http://contextualwebsearch.com/site_search>
   [Peter Thiel]:  <https://en.wikipedia.org/wiki/Peter_Thiel>
   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>



