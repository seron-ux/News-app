from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news,get_news,search_news,get_article
from .forms import ReviewForm
from ..models import Review

Review=Review



# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting news sources
    popularity = get_news('popularity')
    bitcoin = get_news('bitcoin')
    business = get_news('business')
    techcrunch = get_news('techcrunch')
    wall_street = get_news('wsj')

    title = 'Home - Welcome to The best News Review Website Online'

    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('search', category_name = search_news))
    else:
        return render_template('index.html', title = title, popularity = popularity, bitcoin = bitcoin, business = business, techcrunch = techcrunch, wall_street = wall_street )


@main.route('/new/articles/')
def articles():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting news sources
    focus = get_news('focus')
    techcrunch = get_news('techcrunch')
    india = get_news('the-times-of-india')

    title = 'Home - Welcome to The best News Review Website Online'

    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('search', category_name = search_news))
    else:
        return render_template('articles.html', title = title, focus = focus, techcrunch = techcrunch, india = india )





