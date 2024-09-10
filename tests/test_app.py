# Import sys module for modifying Python's runtime environment
import sys
# Import os module for interacting with the operating system
import os

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the Flask app instance from the main app file
from app import app
# Import pytest for writing and running tests
import pytest

@pytest.fixture
def client():
    """Set up a test client for the app with setup and teardown logic."""
    print("\nSetting up the test client")
    with app.test_client() as client:
        yield client  # This is where the testing happens
    print("\nTearing down the test client")

def test_home(client):
    """Test the home route."""
    response = client.get('/')
    assert response.status_code == 200
    # assert response.json == {"message": "Hello, Flask!"}

def test_about(client):
    """Test the about route."""
    response = client.get('/about')
    assert response.status_code == 200
    # assert response.json == {"message": "This is the About page"}

def test_non_existent_route(client):
    """Test for a non-existent route."""
    response = client.get('/non-existent')
    assert response.status_code == 404