import pytest
from app import create_app  # Import the factory function from your 'app' package

@pytest.fixture(scope='module')
def app():
    """
    Module-scoped fixture to create and configure a new app instance.
    This runs once per test module, optimizing performance.
    
    Why 'module' scope? The app configuration is stateless, so we don't 
    need to rebuild it for every single test function.
    """
    
    # Create the app instance using the factory
    app = create_app()

    # Apply specific configurations for the testing environment
    app.config.update({
        "TESTING": True,  # Enables testing mode (e.g., propagates exceptions)
        "WTF_CSRF_ENABLED": False,  # Disable CSRF forms for easier test posting
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",  # Use a fast, in-memory SQLite DB
        "SERVER_NAME": "localhost.localdomain" # Fixes URL generation errors in tests
    })

    # The 'yield' keyword provides the 'app' object to the tests
    yield app

@pytest.fixture
def client(app):
    """
    Request-scoped fixture to get a test client from the app.
    This client allows simulating requests to the application.
    A new client is provided for each test function.
    """
    # app.test_client() is a built-in Flask utility for testing
    return app.test_client()

# --- Smoke Tests (Application Health Checks) ---
# These tests ensure the main pages load without errors.

def test_homepage_loads_successfully(client):
    """
    GIVEN a configured Flask application (via client fixture)
    WHEN the '/' (homepage) route is requested (GET)
    THEN check that the response is valid (HTTP 200 OK)
    """
    response = client.get('/')
    assert response.status_code == 200

def test_homepage_contains_greeting(client):
    """
    GIVEN a configured Flask application
    WHEN the '/' (homepage) route is requested (GET)
    THEN check that the main greeting text is present in the response data
    """
    response = client.get('/')
    # 'b' prefix denotes a byte string, as response.data is in bytes
    assert b"Salut, sunt Iulian!" in response.data 

def test_login_page_loads_successfully(client):
    """
    GIVEN a configured Flask application
    WHEN the '/login' route is requested (GET)
    THEN check that the response is valid (HTTP 200 OK)
    """
    response = client.get('/login')
    assert response.status_code == 200

def test_register_page_loads_successfully(client):
    """
    GIVEN a configured Flask application
    WHEN the '/register' route is requested (GET)
    THEN check that the response is valid (HTTP 200 OK)
    """
    response = client.get('/register')
    assert response.status_code == 200

def test_non_existent_page_returns_404(client):
    """
    GIVEN a configured Flask application
    WHEN a non-existent route is requested (GET)
    THEN check that the response is a 'Not Found' error (HTTP 404)
    """
    response = client.get('/a-page-that-does-not-exist-123')
    assert response.status_code == 404