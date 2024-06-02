"""
pages/a_page.py
----------------
This module contains the code for Page A of the Streamlit app.

The `main` function sets the title and writes a message for Page A.
"""

import streamlit as st


def main():
    """
    This is the main function for Page A of the Streamlit app.
    It sets the title and writes a message for Page A.
    """
    st.title("Heroku Set Up")
    st.write("This page contains instructions for deploying this Streamlit app to Heroku.")
    st.divider()

    # Prerequisites
    st.subheader("Prerequisites")
    st.write(
        "Before deploying this Streamlit app to Heroku, you need to have a Heroku account and the "
        "Heroku CLI installed on your machine. Click on the dropdown below to see instuctions for "
        "installing the Heroku CLI."
    )

    with st.expander("Install Heroku CLI"):
        st.write(
            "Run the following command in the terminal to install the Heroku CLI on your machine:"
        )
        st.code("brew tap heroku/brew && brew install heroku")
    st.divider()

    # Heroku deployment
    st.subheader("Heroku Deployment")
    instructions = """
    #### 1. Create a Staging Heroku App
    1. Log in to Heroku using the Heroku CLI:  
    ```heroku login```
    2. Create the Staging App:  
    ```heroku create your-staging-app-name```  

    *Replace `your-staging-app-name` with the name you want to give your staging app.*  
    
    3. Note Down the App Name and API Key:  
        - The name of the app you created will be used later.  
        - To get the API key, go to the Heroku dashboard [here](https://dashboard.heroku.com/apps), 
    click on the app you created, and go to the `Settings` tab. Click on the `Reveal` button and 
    copy the `API Key` value.
    """  # noqa W291
    st.markdown(instructions)


if __name__ == "__main__":
    main()
