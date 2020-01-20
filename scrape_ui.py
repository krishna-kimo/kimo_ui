import streamlit as st
import os
import pandas as pd
import numpy as np
#import pymongo
import yaml
import requests
import pyyaml

FILE_PATH = "data.yaml"

def get_joke():
    url = 'https://api.chucknorris.io/jokes/random'
    ret = requests.get(url)
    _joke = ret.json()['value']

    return _joke

@st.cache
def get_data():
    with open(FILE_PATH) as file:
        data = yaml.full_load(file)

        return data

def main():
    data = get_data()
    st.title("KIMO Scraping")
    st.markdown("Welcome to the internal world of KIMO where we feed a lot of data for KIMO to learn")

    st.header("Joke for today..")
    st.markdown("> " + get_joke())
    
    keywords_list = ['Machine Learning', 'Natural Language Processing', 'Whats up MF', 'Keyword_3', 'keyword_4', 'keyword_5']
    sample_names = keywords_list[0]
    st_ms = st.multiselect("Keywords", keywords_list, default=sample_names)


if __name__ == '__main__':
    main()
