import urllib.request,json
from .models import News

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

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)


    

    return news_results


    