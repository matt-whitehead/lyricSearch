from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from flask import Flask, render_template, request, Markup
from collections import Counter

# read in the index we created and initialize flask
ix = open_dir('index')
app = Flask(__name__)

def generate_result(query):
    parser = QueryParser('lyrics', ix.schema)
    query = parser.parse(query)

    title = []
    artist = []
    lyrics = []
    genre= []

    with ix.searcher() as searcher:
        results = searcher.search(query)
        for i in results:
            title.append(i['title'])
            artist.append(i['artist'])
            lyrics.append(Markup(i['lyrics'].replace('\n', '<br />')))
            genre.append(i['genre'])

        genre_counts = Counter(genre)

        return title, artist, lyrics, genre, genre_counts

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/search")
def search():
    # collect and parse the query
    q = request.args['q']
    title, artist, lyrics, genre, genre_counts = generate_result(q)

    return render_template("results.html", q=q, title=title, \
        artist=artist, lyrics=lyrics, genre=genre, genre_counts=genre_counts)
