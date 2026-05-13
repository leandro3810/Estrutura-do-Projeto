import pytest

from python import create_app


@pytest.fixture
def client():
    app = create_app({"TESTING": True, "SECRET_KEY": "test"})
    with app.test_client() as client:
        yield client


def test_home(client):
    """Teste para garantir que a rota principal está funcionando."""
    response = client.get("/")
    assert response.status_code == 200


def test_about(client):
    """Teste para garantir que a rota 'about' está funcionando."""
    response = client.get("/about")
    assert response.status_code == 200


def test_health(client):
    """Teste para garantir que a rota de saúde responde corretamente."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "ok", "service": "estrutura-do-projeto"}


def test_not_found_returns_consistent_error(client):
    """Teste para garantir resposta de erro consistente para rotas inexistentes."""
    response = client.get("/nao-existe")
    assert response.status_code == 404
    assert response.json["error"] == "Not Found"


def test_security_headers_present(client):
    """Teste para garantir cabeçalhos de segurança mínimos."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert response.headers["X-Frame-Options"] == "DENY"
    assert "default-src 'self'" in response.headers["Content-Security-Policy"]
