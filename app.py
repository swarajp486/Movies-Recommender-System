
from turtle import pos
import streamlit as st
import pickle
import requests
import webbrowser

movies=pickle.load(open('movies.pkl','rb'))

similarity=pickle.load(open('similarity.pkl','rb'))
def fetch_poster(movie_id):
    
    response=requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=c389fc127d10a4827ff8fe1a5116c4b9&language=en-US")
    data=response.json()
    return  "https://image.tmdb.org/t/p/w500/"+data['poster_path'],data['homepage']

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(enumerate(distances),reverse=True,key=lambda x:x[1])[0:5]
    recommend_movies=[]
    recommend_movies_poster=[]
    recommend_movies_homepage=[]
    for i in movie_list:
        recommend_movies.append(movies.iloc[i[0]].title)
        f_poster,f_homempage=fetch_poster(movies.iloc[i[0]].movie_id)
        recommend_movies_poster.append(f_poster)
        recommend_movies_homepage.append(f_homempage)
    return recommend_movies,recommend_movies_poster,recommend_movies_homepage
st.title("Movie Recommender System")
selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)

# st.write('The current movie title is', title)
if st.button('Recommend'):
    name,poster,homepage=recommend(selected_movie_name)
    col1, col2, col3,col4,col5 = st.columns(5)
    print(name,poster,homepage)

    with col1:
        st.text(name[0])
        st.image(poster[0])
       

        

    with col2:
        st.text(name[1])
        st.image(poster[1])
        
    with col3:
        st.text(name[2])
        st.image(poster[2])
        
        

    

    with col4:
        st.text(name[3])
        st.image(poster[3])
        

    with col5:
        st.text (name[4])
        st.image(poster[4])
    for i in homepage:
        st.markdown(f'{i}', unsafe_allow_html=True)
        
title_name = st.text_input('Movie title')

if st.button('Recommender'):
    # st.text(type(movies['title'].to_string(index=False)))
    if title_name not in movies['title'].to_string(index=False):
        st.text("movie is not found")
    else:  
       
        name,poster,homepage=recommend(title_name)
        col1, col2, col3,col4,col5 = st.columns(5)
        print(name,poster,homepage)

        with col1:
            st.text(name[0])
            st.image(poster[0])
        

            if st.button("home"):
               
               
                js = "window.open('https://www.streamlit.io/')"  # New tab or window
                js = "window.location.href = 'https://www.streamlit.io/'"  # Current tab
                html = '<img src onerror="{}">'.format(js)
                div = Div(text=html)
                st.bokeh_chart(div)


        with col2:
            st.text(name[1])
            st.image(poster[1])
            
        with col3:
            st.text(name[2])
            st.image(poster[2])
            
            

        

        with col4:
            st.text(name[3])
            st.image(poster[3])
            

        with col5:
            st.text (name[4])
            st.image(poster[4])
        for i in homepage:
            
            st.markdown(f'{i}', unsafe_allow_html=True)

