import streamlit as st
st.write("Hello, world!")
'''
import pandas as pd
#from snowflake.snowpark.context import get_active_session
import snowflake.connector
from datetime import datetime, timedelta
#import nltk
#from nltk.tokenize import word_tokenize
import os
from dotenv import load_dotenv
load_dotenv()

if 'SNOWFLAKE_USER' in os.environ:
    snowflake_user = os.getenv('SNOWFLAKE_USER')
    snowflake_password = os.getenv('SNOWFLAKE_PASSWORD')
    snowflake_account = os.getenv('SNOWFLAKE_ACCOUNT')
else:
    # Fallback to Streamlit secrets in production
    snowflake_user = st.secrets["SNOWFLAKE_USER"]
    snowflake_password = st.secrets["SNOWFLAKE_PASSWORD"]
    snowflake_account = st.secrets["SNOWFLAKE_ACCOUNT"]

# Establish the connection
conn = snowflake.connector.connect(
    user=snowflake_user,
    password=snowflake_password,
    account=snowflake_account
)

# Write directly to the app
st.title("La Tortuga Gigante")

def get_data(query):
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

story_portions = get_data("SELECT * FROM educational_technology.stories.la_tortuga_gigante LIMIT 10")

num_segments_shown = 1
#for portion in story_portions:
st.write(story_portions[0][0])
st.write(story_portions[0][1])
'''
