################## Modules ##################
import streamlit as st
from apps.support import *
from apps.scalerSupport import *

def action():
    # Hide stuff
    #hider()

    ################## Read watch list from google sheets ##################
    watch_list = read_sheets('https://docs.google.com/spreadsheets/d/19gx3-AyerS5QNX4HV9ikR-PrOAfLZO0qXLJQ5O6amJg/edit#gid=0', 'id')
    columns    = read_sheets('https://docs.google.com/spreadsheets/d/19gx3-AyerS5QNX4HV9ikR-PrOAfLZO0qXLJQ5O6amJg/edit#gid=148180274', 'columns')
  
    ################## Description #######
    st.sidebar.markdown('''
    **Usabilidade**

    Esta página é dedicada à exploração da base de dados utilizada. 
    Selecione dentre as opções abaixo para customizar seu dashboard.  

    ---
    ''')

    ################## Create sidebar selection with watch_list, period and features ####
    ids      = st.sidebar.multiselect('Selecione as criptomoedas', watch_list, default = [watch_list[9], watch_list[21], watch_list[2], watch_list[30]])
    features = st.sidebar.multiselect('Selecione as métricas', columns, default=[columns[11], columns[0], columns[1]])
    
    st.sidebar.markdown('''
    **Legenda**
    > usd_cp - Preço | dólar

    > eur_mc - Capitalização de mercado | euro

    > brl_tv - Volume | Reais
    
    ---
    ''')
    
    period   = st.sidebar.slider('Defina o periodo | dias', 1, 1100, (1, 365))
    inic     = period[0]
    final    = period[1]

    ################## Create sidebar selection with type of scaler #######
    scalers_dict    = {
                'observado':observed,
                'Growth Scale' :logScaler,
                'Standard Scale': standardScaler,
                'MinMax Scale': mmScaler,
                'Robust Scale': rbstScaler
                }
    scalers = [i for i in scalers_dict]
    scaler = st.sidebar.selectbox('Selecione o método de padronização', scalers)

    ################## Create df #######
    dfs = idJoinerExecuter(ids,features, inic, final)
    for i in range(len(dfs)):
        df = dfs[i]
        df = scalers_dict.get(scaler)(df)
        st.subheader(df.name)
        st.line_chart(df)
    





