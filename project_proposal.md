### Project Proposal of Unsupervised Learning Project
Chien Yuan Chang
#### Question/need:
I am going to use comments from board game players on [Board Game Geek](https://boardgamegeek.com/) to build unsupervised learning models to do analysis and topic modeling and build a recommendation system problem for board game players to find the board games they like.

>* What is the framing question of your analysis, or the purpose of the model/system you plan to build?
>* Who benefits from exploring this question or building this model/system?

#### Data Description:
* Dataset: 
  * I planned to scrape 40 over-500-character comments randomly per game of Top 1500 board games on [Board Game Geek](https://boardgamegeek.com/). However, there were less than 40 comments with more than 500 characters for some games. I tried to decrease the threshold of the games without 40 over-500-character comments and tried to get at least 20 comments for each game. The final dataset contained total 56,951 data points. I will group the comments by the 1500 games. 
 
* An individual sample/unit (total 32 columns):  
	object\_id, username, rating, comment,  
	alias, board\_game\_rank, title, year, geek\_rating,  
	avg\_rating, num\_voters, minplayers, maxplayers,  
	playingtime, minplaytime, maxplaytime,   
	age, age\_2, age\_3, age\_4, age\_5, age\_6, age\_8,  
	age\_10, age\_12, age\_14, age\_16, age\_18, age\_21,   
	usersrated, owned, numcomments
	
	1, 174430, Kylesussenbach, 8, "Pros - Brilliant combat design...",  
	gloomhaven, 1, Gloomhaven, 2017, 8.523,  
	8.76, 46322, 1, 4, 120, 60, 120, 14, 4,  
	0, 0, 0, 0, 5, 41, 80, 127, 17, 2, 3,  
	46322, 75130, 8322

* Expected characteristics/features to work with:
  * comment: The document of the comment. (Over 500 characters)
  * username: The name of the user made the comment  
  * rating: The rating the user gave 
  * year: The year published
  * geek\_rating: Based on the Average Rating, but with artificial votes to prevent games with relatively few votes climbing to the top of the BGG Ranks
  * avg\_rating: The average of all the ratings from registered BGG users
  * num\_voters: The number of users gave the ratings
  * minplayers: The minimum players
  * maxplayers: The maximum players
  * minplaytime: The minimum play time
  * maxplaytime: The maximum play time
  * age: The recommended playing age
  * owned: The number of users who owned the game
  * numcomments: The number of total comments
 
>* What dataset(s) do you plan to use, and how will you obtain the data?
>* What is an individual sample/unit of analysis in this project? What characteristics/features do you expect to work with?

#### Tools:
* Python BeautifulSoup and ElementTree for web scraping
* Python Pandas and Numpy for data clean, data restructuring, exploratory data analysis and feature engineering
* SQLite3 for creating database and table and importing csv into table
* Python SQLAlchemy for querying from the database into Python
* Python NLTK, spaCy and Scikit-learn for text processing
* Other Python libraries or tools if needed

>* How do you intend to meet the tools requirement of the project? 
>* Are you planning in advance to need or use additional tools beyond those required?

#### MVP Goal:
* EDA and Topic Modeling of the comment 

>* What would a minimum viable product (MVP) look like for this project?
