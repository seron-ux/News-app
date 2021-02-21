class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,title,image,description,date,article):
        self.title = title
        self.image = image
        self.description = description
        self.date = date
        self.article = article


class Review:

    all_reviews = []

    def __init__(self,news_id,title,imageurl,review):
        self.news_id = news_id
        self.title = title
        self.imageurl = imageurl
        self.review = review


    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.news_id == id:
                response.append(review)

        return response
