# class Config:
#     '''
#     General configuration parent class
#     '''
#     NEWS_SOURCES_BASE_URL ='https://newsapi.org/v2/sources?apiKey=21b1d83c792a46e6b8cab0cf50d0dbf1'
#     ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey=21b1d83c792a46e6b8cab0cf50d0dbf1'
#     NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
#     SECRET_KEY = os.environ.get('SECRET_KEY')
#     @staticmethod
#     def init_app(app):w
#     pass
# class ProdConfig(Config):
#     pass
# class DevConfig(Config):
#     DEBUG = True
# config_options = {
#     'development': DevConfig,
#     'production': ProdConfig
# }

import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='http://newsapi.org/v2/everything?q={}&from=2020-10-30&sortBy=publishedAt&apiKey={}'
    ARTICLE_API_BASE_URL ='http://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')




class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}    
