from whoosh.index import open_dir
from whoosh.qparser import QueryParser

# read in the index we created
ix = open_dir('index')

# collect and parse the query
query = input('Enter query: ')
parser = QueryParser('lyrics', ix.schema)
query = parser.parse(query)

# search the index and return the results
with ix.searcher() as searcher:
    results = searcher.search(query)
    for i in results:
        print('Title: ' + i['title'])
        print('Artist: ' + i['artist'])
        print('Lyrics: ' + '\n' + i['lyrics'] + '\n')
