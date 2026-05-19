import pytest

from python import create_app


@pytest.fixture
def client():
    app = create_app({"TESTING": True, "SECRET_KEY": "test"})
    assert app.config["TESTING"] is True
    with app.test_client() as client:
        yield client


def test_vary_cookie_added_when_session_accessed_via_request_context():
    """Garante Vary: Cookie quando sessão é acessada via request context."""
    app = create_app({"TESTING": True, "SECRET_KEY": "test"})

    @app.route("/session-request-context")
    def session_request_context():
        from flask.globals import request_ctx

        _ = request_ctx.session
        return "ok"

    with app.test_client() as local_client:
        response = local_client.get("/session-request-context")

    assert response.status_code == 200
    assert "Cookie" in response.vary


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

    top_level_names = {
        item.get("name") for item in payload["structure"] if isinstance(item, dict)
    }
    assert "__pycache__" not in top_level_names
    assert "node_modules" not in top_level_names
    assert not any(
        isinstance(name, str) and name.startswith(".") for name in top_level_names
    )


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
