import pytest
from run import app

@pytest.fixture
def client():
    """Creează un client de test pentru aplicația Flask."""
   #setting the app in testing mode
    app.config.update({
        "TESTING": True,
    })

    #client
    with app.test_client() as client:
        yield client

# tests

def test_homepage_loads_successfully(client):
    """
    Test 1: Verifică dacă pagina principală se încarcă (HTTP 200 OK).
    """
    response = client.get('/') # simulate get request on main page
    assert response.status_code == 200

def test_homepage_contains_greeting(client):
    """
    Test 2: Verifică dacă pagina principală conține textul tău de salut.
    """
    response = client.get('/')
    # 'b' comes from bytes
    assert b"Salut, sunt Iulian!" in response.data 

def test_login_page_loads_successfully(client):
    """
    Test 3: Verifică dacă pagina de login se încarcă.
    """
    response = client.get('/login')
    assert response.status_code == 200

def test_register_page_loads_successfully(client):
    """
    Test 4: Verifică dacă pagina de înregistrare se încarcă.
    """
    response = client.get('/register')
    assert response.status_code == 200

def test_non_existent_page_returns_404(client):
    """
    Test 5: Verifică dacă o pagină falsă returnează "Not Found" (HTTP 404).
    """
    response = client.get('/o-pagina-care-nu-exista-123')
    assert response.status_code == 404