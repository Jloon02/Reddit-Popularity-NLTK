# Reddit Popularity Analysis
What makes a Reddit post popular?

## Our Topic:
How to farm karma and score on Reddit.<br/>
What features should be more emphasized?<br/>
How can we manipulate these feature in a post in order to score higher?

## Required Libraries:
Numpy<br/>
Pandas<br/>
Spark<br/>
Seaborn<br/>
matplotlib<br/>
datetime<br/>
os<br/>
nltk<br/>
'stopwords' from nltk<br/>
'punkt' from nltk<br/>
sklearn<br/>

## Required Commands:
To run the application run the following command:
```
python popularity_prediction.py
```

## Required Arguments:
No arguments are required. However, comments and submissions data must be in the same directory.

## Order of Execution:
Our program will excute the 5 py files under the main file, popularity_prediction.py in this order:
* init_data.py
* read_data.py
* url_analysis.py
* utc_analysis.py
* title_analysis.py

## Files Produced:
There are 3 files produced: A png file ("avg_url_score_withandwithout_zeros") which compares the amount of score a post gets with and without a url in it's body.<br/>
Another png file ("UTC_score_results") that shows the average score a post gets in an hour of the day.<br/>
A txt file ("top_words_title") that lsits the top 25 words to use in your Reddit post's title to get the highest amount of score.

## Files Expected:
txt and png files are expected as the results of our program predictions.

## Notes:
We noticed the feature "score" and "ups" are the same.
Ignored several other columns that did not apply to the problem we are trying to answer.

## Authors
Josh Chung and Nelson Fang
