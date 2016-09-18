# import feedparser
# from flask import Flask
#
# app = Flask(__name__)
#
# # BB = "http://feeds.feedburner.com/breitbart"
# # AT = "http://feeds.arstechnica.com/arstechnica/index"
# # EF = "http://feeds.soundcloud.com/users/soundcloud:users:24638646/sounds.rss"
#
# RSS_FEEDS = {'bb': "http://feeds.feedburner.com/breitbart",
#             'at': "",
#             'ef': "http://feeds.soundcloud.com/users/soundcloud:users:24638646/sounds.rss"}
#
# @app.route("/")
# @app.route("/bb")
# def bb():
#     return get_news('bb')
# @app.route("/at")
# def at():
#     return get_news('at')
#
#
# def get_news(publication):
#     # return "No news is good news"
#     feed = feedparser.parse(RSS_FEEDS[publication])
#     first_article = feed['entries'][0]
#     return """<html>
#         <body>
#             <h1>Headlines</h1>
#             <b>{0}</b><br/>
#             <i>{1}</i><br/>
#             <p>{2}</p><br/>
#         </body>
#     </html>""".format(first_article.get("title"), first_article.get("published"),
#         first_article.get("summary"))
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)

import feedparser
from flask import Flask

app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640',
             'ars': 'http://feeds.arstechnica.com/arstechnica/index' }

@app.route("/")
@app.route("/bbc")
def bbc():
    return get_news('bbc')

@app.route("/cnn")
def cnn():
    return get_news('cnn')

@app.route("/ars")
def ars():
    return get_news('ars')

def get_news(publication):
  feed = feedparser.parse(RSS_FEEDS[publication])
  first_article = feed['entries'][0]
  return """<html>
    <body>
        <h1>Headlines </h1>
        <b>{0}</b> </ br>
        <i>{1}</i> </ br>
        <p>{2}</p> </ br>
    </body>
</html>""".format(first_article.get("title"), first_article.get("published"), first_article.get("summary"))


if __name__ == "__main__":
  app.run(port=5000, debug=True, host='0.0.0.0')
