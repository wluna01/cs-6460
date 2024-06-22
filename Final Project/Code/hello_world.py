import streamlit as st
import pandas as pd
#from snowflake.snowpark.context import get_active_session
import snowflake.connector
from datetime import datetime, timedelta
import nltk
from nltk.tokenize import word_tokenize
from dotenv import load_dotenv
import os

load_dotenv()

snowflake_user = os.getenv('SNOWFLAKE_USER')
snowflake_password = os.getenv('SNOWFLAKE_PASSWORD')
snowflake_account = os.getenv('SNOWFLAKE_ACCOUNT')

# Get the current credentials
#session = get_active_session()
conn = snowflake.connector.connect(
    user=snowflake_user,
    password=snowflake_password,
    account=snowflake_account
)

# Write directly to the app
st.title("La Tortuga Gigante")

cursor = conn.cursor()
cursor.execute("SELECT * FROM educational_technology.stories.la_tortuga_gigante LIMIT 10")
result = cursor.fetchall()
cursor.close()
conn.close()
for row in result:
    st.text(row)
