import requests
import streamlit as st
import webbrowser
def main():
    st.title('Open Playlist Directly On Spotify')
    theplaylist = st.text_input('Enter Your favorite Artist Name')
    clickbutton = st.button('Click Me')

    if clickbutton:
        url = "https://spotify23.p.rapidapi.com/search/"
        querystring = {
            "q": theplaylist,
            "type": "playlists",
            "offset": "0",
            "limit": "10",
            "numberOfTopResults": "5"
        }
        headers = {
            "X-RapidAPI-Key": "aa699afe73msh0b5ec5a9501d381p19948ejsn0881e0164e4c",
            "X-RapidAPI-Host": "spotify23.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        playlistname = response.json()
        name = playlistname['playlists']['items'][0]['data']['uri']
        spotify_uri = name
        webbrowser.open(spotify_uri)

if __name__ == '__main__':
    main()
