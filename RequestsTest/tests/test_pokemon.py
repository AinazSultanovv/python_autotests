import requests
import pytest

# Базовый URL API
BASE_URL = "https://api.pokemonbattle.ru/v2/"
HEADERS = {
    "Content-Type": "application/json",
    "trainer_token": "0d9066e7c4c132e5eb3cc79fc971bd6f"
}

@pytest.fixture(scope="session")
def session():
    """Фикстура для создания сессии"""
    with requests.Session() as session:
        yield session

def test_trainers_status_code(session):
    """Проверяем, что ответ на запрос GET /trainers приходит с кодом 200."""
    url = BASE_URL + "me"
    response = session.get(url, headers=HEADERS)
    assert response.status_code == 200

def test_trainer_name_in_response(session):
    """Проверяем, что в ответе приходит имя тренера."""
    url = BASE_URL + "me" 
    response = session.get(url, headers=HEADERS)
    assert response.status_code == 200
    data = response.json()['data'][0]
    assert data['trainer_name'] == "Swert"  
