import requests
import streamlit as st
st.set_page_config(
    page_title="Malik",
    page_icon="👋",
)
st.title("Get Top 10 Hit Albums Of Artist ")
theartistname = st.text_input('Enter Artist Name')
clickbutton = st.button("click me")
if clickbutton:
    url = "https://spotify23.p.rapidapi.com/search/"

    querystring = {"q":theartistname,"type":"albums","offset":"0","limit":"10","numberOfTopResults":"5"}

    headers = {
        "X-RapidAPI-Key": "aa699afe73msh0b5ec5a9501d381p19948ejsn0881e0164e4c",
        "X-RapidAPI-Host": "spotify23.p.rapidapi.com"
    }

    for i in range(10):  # Change the range to the desired number of iterations
        querystring["offset"] = str(i)  # Update the offset value in the querystring
        response = requests.request("GET", url, headers=headers, params=querystring)
        albumname = response.json()
        name = albumname['albums']['items'][0]['data']['name']
        st.info(name)
