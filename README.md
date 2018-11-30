# lyricssearch
A vertical search engine for song lyrics. Final project for SI 650: Information Retrieval at University of Michigan.
# Installation
* Clone the repository 
* Run ``conda install --file requirements.txt`` in the project directory. You need to have Python 3.6 or newer on [Anaconda](https://www.anaconda.com/download/).
* Download "lyrics.csv" from [Kaggle](https://www.kaggle.com/gyani95/380000-lyrics-from-metrolyrics).
* Run ``mkdir index`` in the project directory.
* Run ``python create_index.py`` in the project directory.
# Usage
* Run ``python main.py`` in the project directory.
* Run ``pip install flask``
* Run ``FLASK_DEBUG=1 FLASK_APP=main.py flask run`` in the project directory. 
* Results are limited to 10 at the moment.
* Then, you can go to [http://127.0.0.1:5000/] to see the search engine in action. 
* **NOTE**: This is a work in progress. The final product will have advanced features such as API integrations.
# TODO
* Index remaining documents.
* Create n-gram model so queries are sensitive to the sequence of lyrics.
* Add advanced search and API integrations.
