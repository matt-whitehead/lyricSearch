from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from flask import Flask, render_template, request, Markup

# read in the index we created
ix = open_dir('index')

app = Flask(__name__)

def generate_result(query):
    parser = QueryParser('lyrics', ix.schema)
    query = parser.parse(query)

    title = []
    artist = []
    lyrics = []

    with ix.searcher() as searcher:
        results = searcher.search(query)
        for i in results:
            title.append(i['title'])
            artist.append(i['artist'])
            lyrics.append(Markup(i['lyrics'].replace('\n', '<br />')))

        return title, artist, lyrics


@app.route("/")
def root():
    return render_template("index.html")

@app.route("/search")
def search():
    # collect and parse the query
    q = request.args['q']
    title, artist, lyrics = generate_result(q)

    return render_template("results.html", q=q, title=title, \
        artist=artist, lyrics=lyrics)
