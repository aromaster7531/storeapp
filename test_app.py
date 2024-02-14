import requests
from app import app  # Assuming your Bottle app is in my_bottle_app.py

def test_welcome():
    """
    Tests the root route with different content types.
    """
    # HTML content
    response = requests.get('http://localhost:8080/')
    assert response.status_code == 200
    assert 'Welcome to DangerWay Market' in response.text

    # Plain text content
    headers = {'Accept': 'text/plain'}
    response = requests.get('http://localhost:8080/', headers=headers)
    assert response.status_code == 200
    assert 'Welcome to DangerWay Market' in response.text

def test_show_list():
    """
    Tests the shopping list route.
    """
    response = requests.get('http://localhost:8080/list')
    assert response.status_code == 200
    assert 'Your Shopping List' in response.text
    assert 'Milk' in response.text
    assert 'Bagel' in response.text
    assert 'Protein Powder' in response.text
    assert 'Cookie Dough' in response.text

def test_add_item():
    """
    Tests adding an item with different cases.
    """
    response = requests.get('http://localhost:8080/add/Cheese/Cheddar')
    assert response.status_code == 200
    assert 'Added item: Cheese, brand: Cheddar to the shopping list' in response.text

    # Case-insensitive item name
    response = requests.get('http://localhost:8080/add/milk/Oat')
    assert response.status_code == 200
    assert 'Added item: milk, brand: Oat to the shopping list' in response.text

    # Existing item with new brand
    response = requests.get('http://localhost:8080/add/Milk/Whole')
    assert response.status_code == 200
    assert 'Added item: Milk, brand: Whole to the shopping list' in response.text

def test_deals():
    """
    Tests the deals listing route.
    """
    response = requests.get('http://localhost:8080/deals')
    assert response.status_code == 200
    assert 'February Deals' in response.text
    assert 'Milk' in response.text
    assert 'Smoked Salmon' in response.text
    assert 'Filet Mignon' in response.text

def test_checkout():
    """
    Tests removing an item with different cases.
    """
    # Existing item
    response = requests.get('http://localhost:8080/checkout/Milk/Lucrene Fat Free')
    assert response.status_code == 200
    assert 'Removed Item: Milk and Brand: Lucrene Fat Free from the shopping list' in response.text

    # Non-existent item
    response = requests.get('http://localhost:8080/checkout/Eggs/Organic')
    assert response.status_code == 200
    assert 'Item: Eggs and Brand: Organic doesn\'t exist.' in response.text

    # Case-insensitive item name
    response = requests.get('http://localhost:8080/checkout/milk/Lucrene')
    assert response.status_code == 200
    assert 'Removed Item: milk and Brand: Lucrene from the shopping list' in response.text

def test_404():
    """
    Tests a non-existent route.
    """
    response = requests.get('http://localhost:8080/not-found')
    assert response.status_code == 404
