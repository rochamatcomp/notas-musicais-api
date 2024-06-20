import pytest
from fastapi.testclient import TestClient
from notas_musicais_api.app import app


@pytest.fixture()
def client():
    return TestClient(app)