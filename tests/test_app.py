"""
This module contains unit tests for the homepage functionality of the app.
"""

from streamlit.testing.v1 import AppTest


def test_homepage():
    """
    Test the homepage functionality of the app.
    """
    at = AppTest.from_file("../Homepage.py").run()
    assert not at.exception  # nosec B101
    assert at.title[0].value == "Welcome to Your App"  # nosec B101
    assert "This is the home page" in at.markdown[0].value  # nosec B101


def test_heroku_set_up_page():
    """
    Test the page A functionality of the app.
    """
    at = AppTest.from_file("../Homepage.py").run()
    at.switch_page("pages/2_Heroku_Set_Up.py").run()
    assert not at.exception  # nosec B101
    assert at.title[0].value == "Heroku Set Up"  # nosec B101
    assert "deploying this Streamlit app to Heroku" in at.markdown[0].value  # nosec B101


def test_github_config_page():
    """
    Test the another page functionality of the app.
    """
    at = AppTest.from_file("../Homepage.py").run()
    at.switch_page("pages/1_GitHub_Configuration.py").run()
    assert not at.exception  # nosec B101
    assert at.title[0].value == "GitHub Configuration"  # nosec B101
    assert "branch protection rules" in at.markdown[0].value  # nosec B101
