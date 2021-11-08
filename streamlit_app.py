import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_distances
#import spacy_streamlit as spacy
#models = ["en_core_web_sm", "en_core_web_md"]
import spacy
nlp = spacy.load('en_core_web_sm')

pca = pickle.load(open('pickles/pca.pkl', 'rb'))
pca_proj = pickle.load(open('pickles/pca_proj.pkl', 'rb'))

#nmf = pickle.load(open('pickles/nmf.pkl', 'rb'))
#nmf_matrix = pickle.load(open('pickles/nmf_matrix.pkl', 'rb'))
title = pickle.load(open('pickles/title.pkl', 'rb'))
tfidf = pickle.load(open('pickles/tfidf.pkl', 'rb'))

st.sidebar.markdown('# Board Game Recommendation System')
eng = st.sidebar.selectbox('Please select a recommendation method', ['Search by Your Description','Preset Keywords'])

if eng == 'Search by Your Description':
    welcome = '''<h4 Please write down the names, types, or any description of the board games you like 
        or just type "game" to get random games. /h4>'''
    st.markdown(welcome, unsafe_allow_html=True)
    des_input = st.text_input("(You can also switch to preset-keyword mode at the sidebar if you don't have any idea for now)")
    if des_input != '':
        flag = 0
        t_nlp = [[w.lemma_.lower() for w in nlp(des_input) 
                  if (not w.is_stop and not w.is_punct and not w.like_num) or (w.lemma_=='not')]]
        for t in t_nlp[0]:
            if t in tfidf.get_feature_names():
                t_clean= [' '.join(w) for w in t_nlp]
                tt = pca.transform(tfidf.transform(t_clean).toarray())
                cos = cosine_distances(tt,pca_proj).argsort()
                #tt = nmf.transform(tfidf.transform(t_clean))
                #cos = cosine_distances(tt,nmf_matrix).argsort()
                game_list =[]
                for g in cos[0][:20]:
                    game_list.append(f"[{title.loc[g, 'title']}](https://boardgamegeek.com/boardgame/{title.loc[g, 'object_id']})")
                for g in game_list:
                    st.markdown(g)
                flag += 1
                break
        if flag == 0:
            st.text('Provided information is not specific enough. Below are random games for your reference!')
            game_list =[]
            for g in np.random.randint(0, 1499, 20):
                game_list.append(f"[{title.loc[g, 'title']}](https://boardgamegeek.com/boardgame/{title.loc[g, 'object_id']})")
            for g in game_list:
                st.markdown(g)
else:
    st.markdown('#### Please select one or more keywords of board games you like')
    key_list = ['solo', 'duo', '2p', '3p', '4p', '5p', '6p', '8p', 
                'action', 'adventure', 'alien', 'animal', 'auction', 'bidding', 
                'card', 'character', 'city building', 'civilization', 'comics',
                'deck', 'dice', 'draft', 'draw', 'dungeon', 'escape', 'expansion', 
                'family', 'ghost', 'hero', 'horror', 'kid',
                'marvel', 'monster', 'pandemic', 'party', 'puzzle', 'quest', 'role', 'rpg', 
                'ship', 'space', 'star trek', 'star war', 'strategy', 'stock', 'story', 
                'team', 'ticket to ride', 'tile', 'train', 'wargame', 'weapon', 'zombie']

    keyword_list = st.multiselect('(You can also switch to self-enter mode at the sidebar to search by your description)', key_list)
    keywords = " ".join(keyword_list)
    if keyword_list != []:
        t_nlp = [[w.lemma_.lower() for w in nlp(keywords) 
                  if (not w.is_stop and not w.is_punct and not w.like_num) or (w.lemma_=='not')]]
        t_clean= [' '.join(w) for w in t_nlp]

        tt = pca.transform(tfidf.transform(t_clean).toarray())
        cos = cosine_distances(tt,pca_proj).argsort()
        #tt = nmf.transform(tfidf.transform(t_clean))
        #cos = cosine_distances(tt,nmf_matrix).argsort()
        game_list =[]
        for g in cos[0][:20]:
            game_list.append(f"[{title.loc[g, 'title']}](https://boardgamegeek.com/boardgame/{title.loc[g, 'object_id']})")
        for g in game_list:
            st.markdown(g)

