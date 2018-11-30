# import required packages and functions
import pandas as pd
from whoosh.index import create_in
from whoosh.fields import *
import whoosh.index

# read in the .csv file to a pandas dataframe
lyrics = pd.read_csv('lyrics.csv')

# identify songs with missing lyrics and drop them from the dataframe
lyrics['is_nan'] = [pd.isna(x) for x in lyrics['lyrics']]
lyrics = lyrics[lyrics['is_nan'] == False]
lyrics = lyrics[['lyrics', 'song', 'artist', 'genre']]
lyrics.reset_index(drop=True, inplace=True)

# clean the artist names and song names
lyrics['artist'] = lyrics['artist'] \
.apply(lambda x: ' '.join(x.split('-')).title())

lyrics['song'] = lyrics['song'].astype('str') \
.apply(lambda x: ' '.join(x.split('-')).title())

# we don't want people to think it's an error in our system
lyrics['genre'].replace('Not Available', 'Unknown', inplace=True)

# only index the first 10,000 documents for prototyping purposes
lyrics_10000 = lyrics.iloc[:10000].copy()

# define the schema
schema = Schema(title=TEXT(stored=True, phrase=True),
                artist=TEXT(stored=True, phrase=True),
                lyrics=TEXT(stored=True, phrase=True),
                genre=TEXT(stored=True, phrase=False))

# create the index
inv_index = create_in('index', schema)
writer = inv_index.writer(limitmb=1000, procs=20)
for row in lyrics_10000.itertuples():
    writer.add_document(title=row[2], artist=row[3], lyrics=row[1], genre=row[4])
writer.commit()
