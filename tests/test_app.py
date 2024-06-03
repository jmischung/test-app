"""
This module contains unit tests for the homepage functionality of the app.
"""

from streamlit.testing.v1 import AppTest


def test_homepage():
    """
    Test the homepage functionality of the app.
    """
    at = AppTest.from_file("../homepage.py").run()
    assert not at.exception  # nosec B101
    assert at.title[0].value == "Welcome to Your App"  # nosec B101
    assert "This is the home page" in at.markdown[0].value  # nosec B101


def test_heroku_set_up():
    """
    Test the page A functionality of the app.
    """
    at = AppTest.from_file("../homepage.py").run()
    at.switch_page("pages/heroku_set_up.py").run()
    assert not at.exception  # nosec B101
    assert at.title[0].value == "Heroku Set Up"  # nosec B101
    assert "deploying this Streamlit app to Heroku" in at.markdown[0].value  # nosec B101


def test_another_age():
    """
    Test the another page functionality of the app.
    """
    at = AppTest.from_file("../homepage.py").run()
    at.switch_page("pages/another_page.py").run()
    assert not at.exception  # nosec B101
    assert at.title[0].value == "Another Page"  # nosec B101
    assert "This is another page" in at.markdown[0].value  # nosec B101
