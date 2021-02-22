import urllib.request,json
from .models import News
import requests

News = News


# Getting api key
api_key = None
# Getting the news base url
base_url = None
base_url2 = None

def configure_request(app):
    global api_key,base_url,base_url2
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    base_url2 = app.config['ARTICLE_API_BASE_URL']

def get_news(category):
    '''
    Function that gets the json responce to our url request
    '''
    get_news_url = base_url.format(category,api_key)
    print(get_news_url)
    get_news_response = requests.get(get_news_url).json()
    print(get_news_response)
    news_results = None

    if get_news_response['articles']:
        news_results_list = get_news_response['articles']
        news_results = process_results(news_results_list)


    

    return news_results


def search_news(news_name):
    search_news_url = 'https://api.thenewsdb.org/3/search/news?api_key={}&query={}'.format(api_key,news_name)
    search_news_response = requests.get(search_news_url).json()
    search_news_results = None

    if search_news_response['results']:
        search_news_list = search_news_response['results']
        search_news_results = process_results(search_news_list)


    return search_news_results


def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects
    Args:
        news_list: A list of dictionaries that contain news details
    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        title = news_item.get('title')
        image = news_item.get('urlToImage')
        description = news_item.get('description')
        date = news_item.get('publishedAt')
        article = news_item.get('url')

        if image:
            news_object = News(title,image,description,date,article)
            news_results.append(news_object)

    return news_results

def get_article(source):
       '''
       Function that gets the json responce to our url request
       '''
       get_news_url = base_url.format(source,api_key)
       with urllib.request.urlopen(get_news_url) as url:
           get_news_data = url.read()
           get_news_response = json.loads(get_news_data)

       news_results = None

       if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)


    

       return news_results


    