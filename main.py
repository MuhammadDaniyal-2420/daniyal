import pip
import requests
import streamlit as st
st.set_page_config(
    page_title="Malik",
    page_icon="👋",
)
st.title("Get Artist Name")
thesongname = st.text_input("Enter song name")
clickbutton = st.button("Click Me")
if clickbutton:
	url = "https://spotify23.p.rapidapi.com/search/"

	querystring = {"q":thesongname,"type":"artists","offset":"0","limit":"10","numberOfTopResults":"5"}

	headers = {
		"X-RapidAPI-Key": "aa699afe73msh0b5ec5a9501d381p19948ejsn0881e0164e4c",
		"X-RapidAPI-Host": "spotify23.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	# print(response.text)
	artistname = response.json()
	name = artistname["artists"]['items'][0]["data"]["profile"]["name"]
	st.info(name)