import pytest
from webtest import TestApp
from app import app as bottle_app 
from urllib.parse import quote



# Define the base URL for the Bottle application
BASE_URL = 'http://localhost:8080'

@pytest.fixture
def client():
    """Create a test client using webtest's TestApp."""
    return TestApp(bottle_app, extra_environ={'wsgi.url_scheme': 'http'})

def test_welcome(client):
    """Test the '/' route."""
    response = client.get(BASE_URL + '/')
    assert response.status_code == 200
    assert 'Welcome to DangerWay Market' in response.text

def test_show_list(client):
    """Test the '/list' route."""
    response = client.get(BASE_URL + '/list')
    assert response.status_code == 200
    assert 'Your Shopping List' in response.text

def test_add_item(client):
    """Test the '/add/<item>/<brand>' route."""
    url = BASE_URL + '/add/' + quote('AppleSauce') + '/' + quote('Kirkland')
    response = client.get(url)
    assert response.status_code == 200
    assert 'Added item: AppleSauce, brand: Kirkland to the shopping list' in response.text

def test_deal_listing(client):
    """Test the '/deals' route."""
    response = client.get(BASE_URL + '/deals')
    assert response.status_code == 200
    assert 'February Deals' in response.text

def test_remove_item(client):
    """Test the '/checkout/<item>/<brand>' route."""
    # Add an item first
    client.get(BASE_URL + '/checkout/AppleSauce/Kirkland')
    
    # Then remove it
    response = client.get(BASE_URL + '/checkout/AppleSauce/Kirkland')
    assert response.status_code == 200
    assert 'Removed Item: AppleSauce and Brand: Kirkland from the shopping list' in response.text

    # Test for non-existent item
    response = client.get(BASE_URL + '/checkout/NonExistentItem/Brand')
    assert response.status_code == 200
    assert 'Item: NonExistentItem and Brand: Brand doesn\'t exist.' in response.text
