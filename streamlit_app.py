import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_distances
#import spacy_streamlit as spacy
#models = ["en_core_web_sm", "en_core_web_md"]
import spacy
nlp = spacy.load('en_core_web_sm')

nmf = pickle.load(open('pickles/nmf.pkl', 'rb'))
nmf_matrix = pickle.load(open('pickles/nmf_matrix.pkl', 'rb'))
title = pickle.load(open('pickles/title.pkl', 'rb'))
tfidf = pickle.load(open('pickles/tfidf.pkl', 'rb'))


eng = st.sidebar.selectbox('Please select a recommendation method', ['Description','Key Words'])

if eng == 'Description':
    des_input = st.text_area('''Please write down the types, themes and description of the board games 
                    you like or just type "game" to get random games''')
    if des_input != '':
        flag = 0
        t_nlp = [[w.lemma_.lower() for w in nlp(des_input) 
                  if (not w.is_stop and not w.is_punct and not w.like_num) or (w.lemma_=='not')]]
        for t in t_nlp[0]:
            if t in tfidf.get_feature_names():
                t_clean= [' '.join(w) for w in t_nlp]
                vt = tfidf.transform(t_clean)
                tt = nmf.transform(tfidf.transform(t_clean))

                cos = cosine_distances(tt,nmf_matrix).argsort()
                game_list =[]
                for g in cos[0][:10]:
                    game_list.append(f"[{title.loc[g, 'title']}](https://boardgamegeek.com/boardgame/{title.loc[g, 'object_id']})")
                for g in game_list:
                    st.markdown(g)
                flag += 1
                break
        if flag == 0:
            st.text('Provided information is not specific enough. Below are a list of random games for your reference')
            game_list =[]
            for g in np.random.randint(0, 1499, 10):
                game_list.append(f"[{title.loc[g, 'title']}](https://boardgamegeek.com/boardgame/{title.loc[g, 'object_id']})")
            for g in game_list:
                st.markdown(g)
else:
    key_list = ['1p', '2p', '3p', '4p', '5p', '6p', '8p', 
            'action', 'adventure', 'alien', 'animal', 'auction', 'bidding', 'card', 'character', 'city building', 'civilization', 
            'deck', 'dice', 'draft', 'draw', 'dungeon', 'escape', 'expansion', 'family', 'ghost', 'hero', 'horror', 'kid',
            'marvel', 'monster', 'pandemic', 'party', 'puzzle', 'quest', 'role', 'rpg', 
            'ship', 'solo', 'space', 'star trek', 'star war', 'strategy', 'stock', 'story', 
            'team', 'ticket to ride', 'tile', 'train', 'wargame', 'weapon', 'zombie']

    keyword_list = st.multiselect('Please select the themes you like', key_list)
    keywords = " ".join(keyword_list)
    if keyword_list != []:
        t_nlp = [[w.lemma_.lower() for w in nlp(keywords) 
                  if (not w.is_stop and not w.is_punct and not w.like_num) or (w.lemma_=='not')]]
        t_clean= [' '.join(w) for w in t_nlp]

        vt = tfidf.transform(t_clean)
        tt = nmf.transform(tfidf.transform(t_clean))

        cos = cosine_distances(tt,nmf_matrix).argsort()
        game_list =[]
        for g in cos[0][:10]:
            game_list.append(f"[{title.loc[g, 'title']}](https://boardgamegeek.com/boardgame/{title.loc[g, 'object_id']})")
        for g in game_list:
            st.markdown(g)

