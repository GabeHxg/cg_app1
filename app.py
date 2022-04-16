from multiapp import MultiApp
import streamlit as st
import apps

# Set wide layout
st.set_page_config(layout="wide")
# import your app modules here
app = MultiApp()

# Add all your application here
app.add_app("Apresentação", apps.pageZero.action)
app.add_app("Documentação", apps.projDetails.action)
app.add_app("Análise Exploratória | Tokens", apps.tokenDashboard.action)
app.add_app("Análise Exploratória | Features", apps.featDashboard.action)

# The main app
app.run()


