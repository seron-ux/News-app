class Config:
    '''
    General configuration parent class
    '''
    NEWS_SOURCES_BASE_URL ='https://newsapi.org/v2/sources?apiKey=21b1d83c792a46e6b8cab0cf50d0dbf1'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey=21b1d83c792a46e6b8cab0cf50d0dbf1'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    @staticmethod
    def init_app(app):w
    pass
class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True
config_options = {
    'development': DevConfig,
    'production': ProdConfig
}