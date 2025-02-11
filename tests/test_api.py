from fastapi.testclient import TestClient

from app.main import app
from app.data.database import get_db, engine, Base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///:memory:"
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

# Sobrescribe la dependencia de la base de datos para las pruebas.
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_signup_and_login():
    import uuid
    # Genera un usuario y email únicos para el test
    unique_username = "testuser_" + str(uuid.uuid4())
    unique_email = f"test_{uuid.uuid4()}@example.com"

    # Registro exitoso
    response = client.post("/api/signup", json={
        "username": unique_username,
        "email": unique_email,
        "password": "secret123"
    })
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["username"] == unique_username

    # Intentar registrar el mismo usuario nuevamente y esperar error
    response_dup = client.post("/api/signup", json={
        "username": unique_username,
        "email": unique_email,
        "password": "secret123"
    })
    assert response_dup.status_code == 400, response_dup.text

    # Login exitoso
    response_login = client.post("/api/login", json={
        "username": unique_username,
        "password": "secret123"
    })
    assert response_login.status_code == 200, response_login.text
    login_data = response_login.json()
    assert "access_token" in login_data


