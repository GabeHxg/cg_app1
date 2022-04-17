import streamlit as st
from multiapp import MultiApp
from apps.pageZero import action as p1 
from apps.projDetails import action as p2
from apps.tokenDashboard import action as p3
from apps.featDashboard import action as p4

# Set wide layout
st.set_page_config(layout="wide")
# import your app modules here
app = MultiApp()

# Add all your application here
app.add_app("Apresentação", p1.action)
app.add_app("Documentação", p2.action)
app.add_app("Análise Exploratória | Tokens", p3.action)
app.add_app("Análise Exploratória | Features", p4.action)

# The main app
app.run()


