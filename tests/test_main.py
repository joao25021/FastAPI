from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_main_get_list():
    response = client.get("/contatos")
    assert response.status_code == 200


def test_create_contato():
    response = client.post(
        "/",
        json={
            "numerodetelefone": 51234,
            "nome": "5string1234",
            "sobrenome": "5string1234",
            "email": "5string1234@"
        },
    )
    assert response.status_code == 200


def test_create_contato_400():
    response = client.post(
        "/",
        json={
            "numerodetelefone": 51234,
            "nome": "5string1234",
            "sobrenome": "5string1234",
            "email": "5string1234@"
        },
    )
    assert response.status_code == 400
