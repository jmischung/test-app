"""
pages/github_config.py
---------------------
This module contains the code for Another Page of the Streamlit app.

The `main` function sets the title and writes a message for Another Page.
"""

import streamlit as st


def main():
    """
    This is the main function for the Another Page of the Streamlit app.
    It sets the title and writes a message for the page.
    """
    st.title("GitHub Configuration")
    st.write("This step walks through configuring branch protection rules in GitHub.")
    st.divider()

    # Branch protection rules
    st.subheader("Branch Protection Rules")
    instructions = """
    1. From the project repository on GitHub, click on the `Settings` tab.
    2. Access Branch Protection Rules:  
        - Click on the `Branches` tab in the left sidebar.
        - Click on the `Add rule` button.
    3. Configure the Branch Protection Rule for `main` branch:  
        - Under `Branch name pattern`, enter `main`.
        - Check the box for `Require pull request reviews before merging` and check the box `Require approvals`.
        - Check `Require status checks to pass before merging` and check the box for `Require branches to be up to date before merging`.
        - In the search box, type the name of the CI/CD workflow that runs on GitHub Actions.  
        *Note: The name of the CI/CD workflow comes from the `ci-cd.yml` file in `.github/workflows`.*
    """  # noqa W291
    st.markdown(instructions)


if __name__ == "__main__":
    main()
