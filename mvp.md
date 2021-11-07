## Recommendation System of Board Games
###### Chien Yuan Chang

The goal of this project is to do analysis and topic modeling to build a recommendation system for board game players to find the board games they like.

To start exploring this goal, I scraped 56,951 comments of top 1500 board games on [Board Game Geek](https://boardgamegeek.com/). Most of the comments were over 500 characters. I did the text preprocessing such as tokenizing, removing numbers, punctuation and stop-words, and lemmatizing. I grouped the comments by the 1500 games and did the topic modeling. I tried count vectorizer and TF-IDF vectorizer with LSA, NMF and LDA and the recommendation system of cosine distance and Euclidean distance. I found the combination of TF-IDF vectorizer, NMF with 21 topics, and cosine distance had the best result. 

The distribution of topics|Vectorizer(Binary)|Vectorizer(Count)|Cosine|Euclidean|
:---|:---|:---|:---|:---
NMF|21 Topics: 0.1%~9.9%|21 Topics: 1.3%~15.3%|Works|Not well
LDA|7 Topics: 0.4%~29.4%|Top Topic: 93.8%|Works|Works
LSA|Top Topic: 100%|Top Topic: 79.8%|-|-

Topic|Keywords| % of Total
:---|:---|:---
Card Drafting|card, hand, draft, draw, round, luck, score, filler, discard, set|15.3%
Strategy Economic|action, cube, area, board, euro, feld, control, round, rondel, selection|8.3%
Wargame|unit, war, wargame, battle, scenario, combat, army, asl, memoir, map|7.4%
Family Cardgame|star, nostar, ize, size, halfstar, x2, x1, gg, x5, thumbsup|7.1%
Dice Rolliing|dice, roll, die, luck, yahtzee, solo, write, number, use, high|6.7%
Thematic Dungeons|dungeon, monster, character, hero, quest, scenario, adventure, campaign, story, miniature|6.1%
Party Word Game|clue, deduction, word, party, werewolf, team, guess, role, codename, people|5.8%
City Building|tile, carcassonne, scoring, score, city, castle, place, lie, azul, board|5.4%
Deck Building|deck, card, dominion, building, expansion, builder, ascension, deckbuilde, villain, deckbuilder|5.3%
Abstract|piece, abstract, dexterity, board, chess, flick, tower, nostar, opponent, gipf|4.9%
Strategy Sci-Fi|worker, placement, resource, building, action, build, caylus, round, euro, place|4.4%
Adventure|pandemic, legacy, story, campaign, op, solo, cooperative, ghost, island, character|4.0%
Ship Space|ship, pirate, wing, alien, planet, captain, trek, crew, space, fleet|3.4%
Auction Bidding|auction, bid, bidding, money, ra, round, win, blind, knizia, value|3.0%
Strategy Wargame|faction, smash, coin, control, summoner, alliance, dune, expansion, area, war|2.3%
Zombie|zombie, zombicide, survivor, alien, scenario, mission, weapon, marine, traitor, human|2.1%
Civilization|civ, civilization, resource, building, city, build, tech, military, technology, race|1.9%
Family Children Animal|animal, agricola, kid, specie, zooloretto, ize, enclosure, dinosaur, zoo, adult|1.7%
Ticket to Ride|ticket, route, ttr, train, ride, passenger, city, map, europe, destination|1.7%
Trains 18xx|company, 18xx, stock, train, share, market, money, dividend, track, loan|1.7%
Puzzle|puzzle, exit, escape, unlock, solve, series, hint, room, clue, app|1.3%

I will use the result of this topic modeling and dimensionality reduction to optimize the content-based recommendation system. 
