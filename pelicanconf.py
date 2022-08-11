import datetime

AUTHOR = 'Eddie Chapman'
SITENAME = 'Out There'
SITESUBTITLE = 'Experimental arts series'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'America/Chicago'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%B %-d, %Y'

DEFAULT_LANG = 'en'

DELETE_OUTPUT_DIRECTORY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False


def date_past(event_date):
    return datetime.date.fromisoformat(event_date) < datetime.date.today()


def date_future(event_date):
    return not date_past(event_date)


def future_events(iterable):
    return reversed([event for event in iterable if date_future(event.metadata["event-date"])])


def past_events(iterable):
    return (event for event in iterable if date_past(event.metadata["event-date"]))


def format_date(date_string):
    date_obj = datetime.date.fromisoformat(date_string)
    return date_obj.strftime('%B %-d, %Y')


def news_articles(categories):
    for category, articles in categories:
        if category.name == "news":
            return articles


# def future_events(categories):
#     for category, articles in categories:
#         if category.name == "events":
#             for article in articles:
#                 event_date = datetime.date.fromisoformat(article.metadata["event-date"])
#                 if event_date >= datetime.date.today():
#                     yield article


# def past_events(categories):
#     for category, articles in categories:
#         if category.name == "events":
#             for article in articles:
#                 event_date = datetime.date.fromisoformat(article.metadata["event-date"])
#                 if event_date < datetime.date.today():
#                     yield article



JINJA_TESTS = {
    "date_past": date_past,
    "date_future": date_future,
}

JINJA_FILTERS = {
    "future_events": future_events,
    "past_events": past_events,
    "format_date": format_date,
    "news_articles": news_articles
}