import pytest

from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    with app.test_client() as _client:
        yield _client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<h1>Hello, World!</h1>' in response.data
    assert b'Welcome to this beautiful HTML page rendered with Flask.' in response.data
