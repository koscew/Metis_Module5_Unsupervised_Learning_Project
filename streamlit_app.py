import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_distances
import spacy
nlp = spacy.load('en_core_web_sm')

#nmf = pickle.load(open('pickles/nmf.pkl', 'rb'))
#nmf_matrix = pickle.load(open('pickles/nmf_matrix.pkl', 'rb'))
with open('pickles/pca.pkl', 'rb') as f:
    pca = pickle.load(f)
with open('pickles/pca_proj.pkl', 'rb') as f:
    pca_proj = pickle.load(f)
with open('pickles/title.pkl', 'rb') as f:
    title = pickle.load(f)
with open('pickles/tfidf.pkl', 'rb') as f:
    tfidf = pickle.load(f)

st.sidebar.markdown('# Board Game Recommendation System')
st.sidebar.write('(A NLP model built on BGG player comments)')
eng = st.sidebar.selectbox('Please select a recommendation method', ['Search by Your Own Words','Preset Keywords'])

st.sidebar.write('Filters (refresh the page to clear the filters)')
min_rating = st.sidebar.slider('Minimum Ratings', 6.0, 9.0, 6.0, 0.01)
year = st.sidebar.slider('Published Year', 1980, 2021, (1980,2021))
player_min = st.sidebar.slider('Minimum Players', 1, 8, 1)
player_max = st.sidebar.select_slider('Maximum Players', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 16, 20, 30, 100], 100)
time_min = st.sidebar.select_slider('Minimum Play Time', [2, 5, 10, 15, 20, 30, 45, 60, 120, 240, 480, 720], 2)
time_max = st.sidebar.select_slider('Maximum Play Time', [2, 5, 10, 15, 20, 30, 45, 60, 120, 240, 480, 720, 12000], 12000)
age_suggest = st.sidebar.slider('Suggest Minimum Age', 0, 18, (0,18))
age_com = st.sidebar.slider('Suggest Minimum Age by the BGG Community', 0, 18, (0,18))
own = st.sidebar.slider('Game Owners on BGG', 300, 165000, (300, 165000), 100)

title_fil = title[(title['avg_rating'] >= min_rating) &
                  (title['year'] >= year[0]) & (title['year'] <= year[1]) &
                  (title['minplayers'] >= player_min) & (title['maxplayers'] <= player_max) & 
                  (title['minplaytime'] >= time_min) & (title['maxplaytime'] <= time_max) &
                  (title['age'] >= age_suggest[0]) & (title['age'] <= age_suggest[1]) &
                  (title['com_age'] >= age_com[0]) & (title['com_age'] <= age_com[1]) &
                  (title['owned'] >= own[0]) & (title['owned'] <= own[1])]
                  
st.sidebar.write(f'Total: {len(title_fil)} games')

if eng == 'Search by Your Own Words':
    welcome = '''Please write down the names, types, or any description of the board games you like \
    or just type "game" to get random games.'''
    st.markdown(f'#### {welcome}')
    des_input = st.text_input("(You can also switch to preset-keyword mode at the sidebar if you don't have any idea for now)")
    if des_input != '':
        flag = 0
        t_nlp = [[w.lemma_.lower() for w in nlp(des_input) 
                  if not w.is_stop and not w.is_punct and not w.like_num]]
        for t in t_nlp[0]:
            if t in tfidf.get_feature_names():
                t_clean= [' '.join(w) for w in t_nlp]
                tt = pca.transform(tfidf.transform(t_clean).toarray())
                cos = cosine_distances(tt,pca_proj).argsort()
                #tt = nmf.transform(tfidf.transform(t_clean))
                #cos = cosine_distances(tt,nmf_matrix).argsort()
                game_list =[]
                for g in cos[0]:
                    if len(game_list) < 20:
                        try:
                            game_list.append(f"[{title_fil.loc[g, 'title']}](https://boardgamegeek.com/boardgame/{title_fil.loc[g, 'object_id']})")
                        except Exception:
                            pass
                for g in game_list:
                    st.markdown(g)
                flag += 1
                break
        if flag == 0:
            st.write('Provided information is not specific enough. Below are random games for your reference!')
            game_list =[]
            arr = np.arange(1500)
            np.random.shuffle(arr)
            for g in arr:
                if len(game_list) < 20:
                    try:
                        game_list.append(f"[{title_fil.loc[g, 'title']}](https://boardgamegeek.com/boardgame/{title_fil.loc[g, 'object_id']})")
                    except Exception:
                        pass
            for g in game_list:
                st.markdown(g)
else:
    st.markdown('#### Please select one or more keywords of board games you like')
    key_list = ['action', 'adventure', 'alien', 'ancient', 'animal', 'area control', 'auction', 'army', 
                'battle', 'bidding', 'car', 'card', 'character', 'city building', 'civilization', 'comics', 'cute',
                'deck', 'dice', 'draft', 'draw', 'dungeon', 'economic', 'escape', 'expansion', 
                'family', 'ghost', 'gold', 'guess', 'hero', 'horror', 'kid',
                'luck', 'magic', 'majority', 'marvel', 'mission', 'monster', 
                'pandemic', 'party', 'planet', 'puzzle', 'quest', 'racing', 'role', 'rpg', 
                'scenario', 'ship', 'solo', 'space', 'star trek', 'star war', 'strategy', 'stock', 'story', 
                'team', 'ticket to ride', 'tile', 'train', 'wargame', 'weapon', 'zombie']

    keyword_list = st.multiselect('(You can also switch to self-enter mode at the sidebar to search by your description)', key_list)
    keywords = " ".join(keyword_list)
    if keyword_list != []:
        t_nlp = [[w.lemma_.lower() for w in nlp(keywords) 
                  if not w.is_stop and not w.is_punct and not w.like_num]]
        t_clean= [' '.join(w) for w in t_nlp]

        tt = pca.transform(tfidf.transform(t_clean).toarray())
        cos = cosine_distances(tt,pca_proj).argsort()
        #tt = nmf.transform(tfidf.transform(t_clean))
        #cos = cosine_distances(tt,nmf_matrix).argsort()
        game_list =[]
        for g in cos[0]:
            if len(game_list) < 20:
                try:
                    game_list.append(f"[{title_fil.loc[g, 'title']}](https://boardgamegeek.com/boardgame/{title_fil.loc[g, 'object_id']})")
                except Exception:
                    pass
        for g in game_list:
            st.markdown(g)

