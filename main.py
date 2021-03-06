from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from flask import Flask, render_template, request, Markup, url_for
from collections import Counter

# read in the index we created and initialize flask
ix = open_dir('index')
app = Flask(__name__)


def generate_result(query, search_type):
    # parse the query and search 'lyrics' field
    if search_type == 'lyrics':
        parser = QueryParser('lyrics', ix.schema)
        phrase_query = '"' + query + '"'
        parsed = parser.parse(phrase_query)
        raw_parsed = parser.parse(query)
    elif search_type == 'artist':
        parser = QueryParser('artist', ix.schema)
        parsed = parser.parse(query)
        raw_parsed = parsed
    elif search_type == 'title':
        parser = QueryParser('title', ix.schema)
        parsed = parser.parse(query)
        raw_parsed = parsed
    else:
        raise ValueError('Invalid Search Type: ' + search_type)

    # initialize lists for the results
    title = []
    artist = []
    lyrics = []
    genre = []

    # open a searcher object
    with ix.searcher() as searcher:
        # attempt to correct the query
        corrected = searcher.correct_query(raw_parsed, query)
        results = searcher.search(parsed)
        # if the corrected query isn't the same as the original query...
        if corrected.query != raw_parsed:
            modified_query = corrected.string
            modified_query = Markup('<a href=' + url_for('search', t=search_type, q=modified_query) + '>' + corrected.string + '</a>')
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
    q = request.args['q']  # query
    t = request.args['t']  # type

    title, artist, lyrics, genre, genre_counts, modified_query = generate_result(q, t)

    return render_template("results.html", q=q, title=title,
                           artist=artist, lyrics=lyrics, genre=genre,
                           genre_counts=genre_counts, modified_query=modified_query, t=t)

def filterByGenre():
    g = request.args['g']  # genre

    # if button clicked == genre
    # call generate_result function to only search for these genreSelected
    # then render_template 

    return 0
