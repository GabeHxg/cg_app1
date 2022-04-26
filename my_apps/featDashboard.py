################## Modules ##################
import streamlit as st
import plotly.express as px
from my_apps.support import *
from my_apps.scalerSupport import *
from my_apps.decomposerSupport import *

def action():
    # Hide stuff
    #hider()

    ################## Read watch list from google sheets ##################
    watch_list = read_sheets('https://docs.google.com/spreadsheets/d/19gx3-AyerS5QNX4HV9ikR-PrOAfLZO0qXLJQ5O6amJg/edit#gid=0', 'id')
    columns    = read_sheets('https://docs.google.com/spreadsheets/d/19gx3-AyerS5QNX4HV9ikR-PrOAfLZO0qXLJQ5O6amJg/edit#gid=148180274', 'columns')

    # Space out the maps so the first one is 2x the size of the other three
    c1, c2= st.columns(2)

    ################## Create selection with token, period and features ####
    st.markdown('---')
    ids      = c1.multiselect('Selecione as criptomoedas', watch_list, default = [watch_list[9], watch_list[5], watch_list[20]])
    features = c2.multiselect('Selecione as métricas', columns, default=[columns[11], columns[1]])
    period   = c2.slider('Defina o periodo de análise | dias', 1, 1100, (1, 1100))
    inic     = period[0]
    final    = period[1]

    ################## Create selection with type of scaler #######
    scalers_dict    = {
                'Observado':observed,
                'Metcalfe Scale' :logScaler,
                'Standard Scale': standardScaler,
                'MinMax Scale': mmScaler,
                'Robust Scale': rbstScaler
                }
    scalers = [i for i in scalers_dict]
    scaler = c1.selectbox('Selecione o método de padronização', scalers)

    ################## Create selection with type of Decomposer and Period#######
    decomp_dict    = {
                'Observado':Observed,
                'Tendência' :Trend,
                'Sazonalidade': Seasonal,
                'Resíduo': Resid
                }    
    decomposers = [i for i in decomp_dict]
    decomposer = c1.selectbox('Selecione o método de decomposição', decomposers)
    dec_period = c2.slider('Defina o periodo de decomposição | dias',  1, 365, 7)
   
    
    ################## Create df #######
    dfs = featsJoinerExecuter(ids,features, inic, final)

    ######## Progress Bar ######
    st.subheader('Querying progress')
    my_bar = st.progress(0)

    ######## For loop ########
    for i in range(len(dfs)):
        df = dfs[i]
        df = scalers_dict.get(scaler)(df)
        dec_df = decomp_dict.get(decomposer)(df, dec_period)
        
        st.subheader(df.name)
        fig = px.line(dec_df, 
                      x=dec_df.index, 
                      y=dec_df.columns,
                      color_discrete_sequence=px.colors.qualitative.Set1, 
                      line_dash_sequence=['longdashdot','dash'],
                      template="plotly_dark")
                      
        fig.update_layout(autosize=True)#,height=300,width=1200)
        st.write(fig)
        my_bar.progress(i/len(dfs))
    my_bar.progress(100)
