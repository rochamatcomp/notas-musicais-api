"""
Tests for app.
"""

from http import HTTPStatus

from fastapi.testclient import TestClient

from notas_musicais_api.app import app


def test_root_must_response_hello_message():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá, Notas musicais!'}
