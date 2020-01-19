import streamlit as st
import os
import pandas as pd
import numpy as np
import pymongo

#@st.cache(allow_output_mutation=True)
def get_records():
    record = {}
    record['id'] = '1234'
    record['source'] = 'Medium'
    record['summary'] = 'This is summary'
    record['upvotes'] = 35
    record['keywords'] = ['Google', 'Amazon', 'Machine Learning', 'Algorithms', 'Random Stuff']

    return record

if __name__ == '__main__':
    print(get_records())
