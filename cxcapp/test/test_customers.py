import uuid

from fastapi import status


def test_create_customer(client):
    # Setup: generar email único
    email = f"{uuid.uuid4()}@example.com"

    # Test: crear cliente
    response = client.post(
        "/customers",
        json={
            "name": "Jhon Doe",
            "email": email,
            "age": 33,
        },
    )
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["name"] == "Jhon Doe"
    assert data["email"] == email
    assert data["age"] == 33


def test_get_customer_by_id(client):
    # Setup: crear cliente
    email = f"{uuid.uuid4()}@example.com"
    response = client.post(
        "/customers",
        json={
            "name": "Jane Smith",
            "email": email,
            "age": 28,
        },
    )
    assert response.status_code == status.HTTP_201_CREATED
    customer_id = response.json()["id"]

    # Test: leer cliente por ID
    response_read = client.get(f"/customers/{customer_id}")
    assert response_read.status_code == status.HTTP_200_OK
    data = response_read.json()
    assert data["name"] == "Jane Smith"
    assert data["email"] == email
    assert data["age"] == 28
