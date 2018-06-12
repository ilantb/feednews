import bottle as b
from bottle import route, run, get, request, response
import json
import feedparser
from datetime import datetime


feed = feedparser.parse("https://www.jpost.com/Rss/RssFeedsHeadlines.aspx")

@route('/')
def index():
    return b.template('Week10L3ex1.html')


@get('/api/getNews')
def get_news():
    listNews = list()
    for element in feed["entries"]:
        listNews.append({"title": element["title"], "link": element["link"]})
    return json.dumps(listNews)


def main():
    run(host='localhost', port=7000)


if __name__ == '__main__':
    main()

