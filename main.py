import streamlit as st
import hompage
import test

# Initialize the session state if it does not exist
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Load the appropriate page based on session state
if st.session_state.page == 'home':
    hompage.app()
elif st.session_state.page == 'test':
    test.app()