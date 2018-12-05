from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from flask import Flask, render_template, request, Markup, url_for
from collections import Counter

# read in the index we created and initialize flask
ix = open_dir('index')
app = Flask(__name__)


def generate_result(query):
    # parse the query and search 'lyrics' field
    parser = QueryParser('lyrics', ix.schema)
    query = '"' + query + '"'
    parsed = parser.parse(query)

    # initialize lists for the results
    title = []
    artist = []
    lyrics = []
    genre = []

    # open a searcher object
    with ix.searcher() as searcher:
        # attempt to correct the query
        corrected = searcher.correct_query(parsed, query)
        results = searcher.search(parsed)
        # if the corrected query isn't the same as the original query...
        if corrected.query != parsed:
            modified_query = corrected.string
            modified_query = Markup('<a href=' + url_for('search', q=modified_query) + '>' + corrected.string + '</a>')
        else:
            modified_query = None
        # process the results and put them into the lists
        for i in results:
            title.append(i['title'])
            artist.append(i['artist'])
            lyrics.append(Markup(i['lyrics'].replace('\n', '<br />')))
            genre.append(i['genre'])

        # count up the genres of the results
        genre_counts = Counter(genre)

        return title, artist, lyrics, genre, genre_counts, modified_query


@app.route("/")
def root():
    return render_template("index.html")


@app.route("/search")
def search():
    # collect and parse the query
    q = request.args['q']
    title, artist, lyrics, genre, genre_counts, modified_query = generate_result(q)

    return render_template("results.html", q=q, title=title,
                           artist=artist, lyrics=lyrics, genre=genre,
                           genre_counts=genre_counts, modified_query=modified_query)
