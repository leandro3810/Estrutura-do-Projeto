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


def test_project_structure_api(client):
    """Teste para garantir que a API de estrutura do projeto responde corretamente."""
    response = client.get("/api/project-structure")
    assert response.status_code == 200

    payload = response.get_json()
    assert isinstance(payload, dict)
    assert "root" in payload
    assert "generated_at" in payload
    assert isinstance(payload.get("structure"), list)
