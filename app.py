from multiapp import MultiApp
import streamlit as st
from apps import pageZero, projDetails, tokenDashboard, featDashboard

# Set wide layout
st.set_page_config(layout="wide")
# import your app modules here
app = MultiApp()

# Add all your application here
app.add_app("Apresentação", pageZero.action)
app.add_app("Documentação", projDetails.action)
app.add_app("Análise Exploratória | Tokens", tokenDashboard.action)
app.add_app("Análise Exploratória | Features", featDashboard.action)

# The main app
app.run()


