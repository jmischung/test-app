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
    1. Create the Staging and Production Apps
        - Log in to Heroku using the Heroku CLI:  
        ```heroku login```
        - Create the Staging App:  
        ```heroku create your-staging-app-name```  
        - Create the Production App:  
        ```heroku create your-production-app-name```        

    2. Create the Pipeline
        - Create the Pipeline:  
        The command must specify an existing app to be added to the pipeline.  
        ```heroku pipelines:create -a your-staging-app-name```
        - Add the Production App to the Pipeline:  
        ```heroku pipelines:add your-pipeline-name -a your-production-app-name```  

    3. Configure the Pipeline  
        - From the Heroku dashboard, go to the pipeline and click on the settings tab.
        - In the `Connect to GitHub` section, connect the pipeline to the GitHub repository.  
        - In the `Review apps` section, enable review apps. Check the boxes for 'Create new review
        apps for new pull requests...', 'Wait for CI to pass', and 'Destroy stale review apps'.  
        - in the `Heroku CI` section, enable Heroku CI.  

    At this point, the pipeline should look something like this:
    """  # noqa W291
    st.markdown(instructions)
    st.image("images/heroku_pipeline.png", use_column_width=True)


if __name__ == "__main__":
    main()
