################## Modules ##################
import streamlit as st
import pandas as pd

################## Cloud Connect ##################
from google.oauth2 import service_account
from google.cloud import bigquery

################## Create API client ##################
credentials = service_account.Credentials.from_service_account_info(st.mySecrets['gcp_service_account'])
client = bigquery.Client(credentials=credentials)

################# Define function to hide stuff #######
def hider():
    # Hide stuff
    hide_menu_style = '''
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
    '''
    st.markdown(hide_menu_style, unsafe_allow_html = True)

########### Funtion to read Google Sheet CSVs ##########
def read_sheets(url, col):
    tb = url.replace('/edit#gid=', '/export?format=csv&gid=')
    df = pd.read_csv(tb)
    df = list(df[col])
    return df

########### Funtion to retrieve tokens database from Google BigQuery ##########
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=60000)
def run_query(id, feature):
    query = f'SELECT dates, {feature} FROM awaricripto.awaricripto_timeSeries.{id}'
    query_job = client.query(query)
    rows_raw = query_job.result()

    # Convert to list of dicts. Required for st.experimental_memo to hash the return value.
    rows = [dict(row) for row in rows_raw]
    rows = pd.DataFrame(rows)
    rows = rows.set_index('dates')
    return rows
    

########### Funtion to Join other currencies ##########
def idJoiner(ids, feature):
    # Create empty df
    joined_df = pd.DataFrame()

    # Iterate over list of currencies 
    for id in ids:
        joined_df[f'{id}'] = run_query(id, feature)
    
    return joined_df


########### Funtion to execute idJoiner ##########
def idJoinerExecuter(ids,features,inic,final):
    df_lst = []
    for feature in features:
        # build joined dataframe
        df = idJoiner(ids,feature)
        df = df.iloc[inic:final]
        df.name = feature
        df_lst.append(df)
    return df_lst


########### Funtion to Join other features ##########
def featsJoiner(id, features):
    # Create empty df
    joined_df = pd.DataFrame()

    # Iterate over list of features
    for feature in features:
        joined_df[f'{feature}'] = run_query(id, feature) 

    return joined_df

########### Funtion to execute featsJoiner ##########
def featsJoinerExecuter(ids,features,inic,final):
    df_lst = []
    for id in ids:
        # build joined dataframe
        df = featsJoiner(id,features)
        df = df.iloc[inic:final]
        df.name = id
        df_lst.append(df)
    return df_lst
