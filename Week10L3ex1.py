import bottle as b
from bottle import route, run, get, request, response
import json
import feedparser
from datetime import datetime, timedelta


feed = feedparser.parse("https://www.jpost.com/Rss/RssFeedsHeadlines.aspx")

@route('/')
def index():
    return b.template('Week10L3ex1.html')


@get('/api/getNews')
def get_news():
    now_time = str(datetime.now())
    if request.get_cookie("last_log") :
        msg = "Welcome back, your last visit was : ", request.get_cookie("last_log")
        response.set_cookie("last_log", now_time)
    else :
        expire_time = datetime.now()+timedelta(days=13)
        response.set_cookie("last_log", now_time, expires = expire_time)
        msg = "Welcome to rss"
    listNews = list()
    for element in feed["entries"]:
        listNews.append({"title": element["title"], "link": element["link"]})
    return json.dumps([listNews,msg])


def main():
    run(host='localhost', port=7000)


if __name__ == '__main__':
    main()

