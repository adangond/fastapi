from fastapi.testclient import TestClient


def test_client_instance(client):
    assert isinstance(client, TestClient)
