"""
your_homepage.py
----------------
This module contains the code for the home page of the Streamlit app.

The main function sets the page configuration, displays the title, and writes a
message on the home page of the app.
"""
import streamlit as st


def main():
    """
    Main function to run the Streamlit app.

    This function sets the page configuration, displays the title, and writes a
    message on the home page of the app.
    """
    st.set_page_config(page_title="Your App Name", page_icon=":guardsman:", layout="wide")
    st.title("Welcome to Your App")
    st.write("This is the home page of your Streamlit app.")


if __name__ == "__main__":
    main()
