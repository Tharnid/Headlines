import feedparser
from flask import Flask

app = Flask(__name__)

BB = "http://feeds.feedburner.com/breitbart"
AT = "http://feeds.arstechnica.com/arstechnica/index"
EF = "http://feeds.soundcloud.com/users/soundcloud:users:24638646/sounds.rss"


@app.route("/")
def get_news():
    # return "No news is good news"
    feed = feedparser.parse(EF)
    first_article = feed['entries'][0]
    return """<html>
        <body>
            <h1>Headlines</h1>
            <b>{0}</b><br/>
            <i>{1}</i><br/>
            <p>{2}</p><br/>
        </body>
    </html>""".format(first_article.get("title"), first_article.get("published"),
        first_article.get("summary"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
