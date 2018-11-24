# lyricssearch
A vertical search engine for song lyrics. Final project for SI 650: Information Retrieval at University of Michigan.
# Installation
* Clone the repository 
* Run ``conda install --file requirements.txt`` in the project directory. You need to have Python 3.6 or newer on [Anaconda](https://www.anaconda.com/download/)
* Download "lyrics.csv" from [Kaggle](https://www.kaggle.com/gyani95/380000-lyrics-from-metrolyrics).
* Run ``mkdir index`` in the project directory.
* Run ``python create_index.py`` in the project directory.
# Usage
* Run ``python main.py`` in the project directory.
* Type in your query and push enter.
* Results are limited to 10 at the moment.
* **NOTE**: This is a work in progress. The final product will have a UI and advanced features.
# TODO
* Index remaining documents.
* Create n-gram model so queries are sensitive to the sequence of lyrics.
* Create UI.
* Add advanced search and API integrations.
* Come up with a better name lol.
