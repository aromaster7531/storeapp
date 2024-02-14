import requests

def test_welcome():
    response = requests.get('http://localhost:8080/')
    assert response.status_code == 200
    assert 'Welcome to DangerWay Market' in response.text

def test_show_list():
    response = requests.get('http://localhost:8080/list')
    assert response.status_code == 200
    assert 'Your Shopping List' in response.text
    assert 'Milk' in response.text
    assert 'Bagel' in response.text
    assert 'Protein Powder' in response.text
    assert 'Cookie Dough' in response.text
