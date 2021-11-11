# Board Game Recommendation System
Chien Yuan Chang

## Abstract
The goal of this project was to do analysis and topic modeling to build a recommendation system for users to find the board games they may like. 

I scraped 56,951 comments of top 1500 board games on [BoardGameGeek](https://boardgamegeek.com/). Most of the comments were over 500 characters. I did the text preprocessing such as tokenizing, removing foreign language, numbers, punctuation and stop-words, and lemmatizing. I grouped the comments by the 1500 games and tried count vectorizer and TF-IDF vectorizer with LSA, NMF, LDA and PCA to build the recommendation system of cosine distance and Euclidean distance. I found the combination of TF-IDF vectorizer, PCA with 600 components, and cosine distance had the best result. I packed the models and deployed the system on [Streamlit](https://share.streamlit.io/koscew/metis_module5_unsupervised_learning_project/main). 

This personalized and customized recommendation system allows the users to get the recommendation immediately at any time and location and is better than title search.

## Design
Due to the pandemic, most people have spent more time at home. Board games can be good entertainment at home. We can have less screen time and more connections and great moments with family members and friends. It can also be good lessons for children and good for adult brain function. However, there are more than 130,000 board games on BoardGameGeek. A board game recommendation system which the users can input by themselves to get the recommendation immediately at any time and location would help people find the games they will like. 

## Data
I planned to scrape 40 over-500-character comments randomly per game of Top 1500 board games on [BoardGameGeek](https://boardgamegeek.com/). I scraped the list of top 1500 games first and then scraped the stats and comments on webpages of [BoardGameGeek XML API](https://boardgamegeek.com/wiki/page/BGG_XML_API#). However, there were less than 40 comments with more than 500 characters for some games. I tried to decrease the threshold of the games without 40 over-500-character comments and tried to get at least 20 comments for each game. The final dataset contained a total 56,951 data points and 32 features. The main feature was text data of the comments. The data of average rating, year, minimum players, maximum players, minimum play time, maximum play time, suggested age, suggested age and number of owners on BGG was used as a filter on the recommendation system.

## Algorithms

***Natural Language Processing***

1. Used spaCy and its language detect package to detect and remove 3634 data points of foreign language
2. Used spaCy to lemmatize, lowercase and remove stopwords, numbers and punctuations
3. Group the comments of 53,317 data points by 1500 games 
4. Used vectorizer for the models


***Topic Modeling***

Latent Semantic Analysis (LSA), Latent Dirichlet Allocation (LDA), Non-negative matrix factorization (NMF) and Correlation Explanation (CorEx) were tried for topic modeling. The combination of TF-IDF vectorizer and NMF with 21 topics had the best result. The keywords from NMF topic modeling were used as preset keywords for users to select on the recommendation system.

***Recommendation System***

Among dimensionality reduction algorithms, the combination of TF-IDF vectorizer, Principal Component Analysis (PCA) with 600 components and 80% variance explained, and cosine distance had the best performance of the recommendation system.

***Application Deploy***
  
Streamlit was used to build the application and visualize the recommendation system. The models of TF-IDF vectorizer and PCA, the PCA matrix, and the dataframe of the stats of board game were packed and loaded by pickle. The application has 2 modes. The users can choose to either input their own words or select preset keywords. The preset keywords were from NMF topic modeling. The user can also filter the board games by published year, number of players, play time, suggested age, and the popularity.

## Tools
- Python BeautifulSoup and ElementTree for web scraping
- Python Pandas and Numpy for data clean, data restructuring, exploratory data analysis and feature engineering
- Python NLTK, spaCy for text processing
- Python Scikit-learn for vectorization, topic modeling, dimensionality reduction, clustering
- Python Matplotlib, Seaborn and pyLDAvis for data visualization
- Python Pickle for packaging the models, matrices and data
- Python Streamlit for visualization and web application

## Communication
In addition to [the slides of the final presentation](final_presentation.pdf), [charts](images/), and this written description, the recommendation system was deployed on [Streamlit](https://share.streamlit.io/koscew/metis_module5_unsupervised_learning_project/main) and the findings will also be posted on [my personal blog](https://koscew.github.io/) in the future.
