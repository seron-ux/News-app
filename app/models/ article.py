class Article:

    all_article = []

def __init__(self,news_id,title,imageurl,review):
        self.news_id = news_id
        self.title = title
        self.imageurl = imageurl
        self.article = article


def save_article(self):
        Article.all_article.append(self)


@classmethod
def clear_article(cls):
        Article.all_article.clear()

@classmethod
def get_article(cls,id):

        response = []

        for article in cls.all_article:
            if article.news_id == id:
                response.append(article)

        return response    