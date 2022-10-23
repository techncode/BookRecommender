from app import app
import sys


def test_home_page():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert "<h1>Discover books you'll love!</h1>" in response.data.decode('utf-8')