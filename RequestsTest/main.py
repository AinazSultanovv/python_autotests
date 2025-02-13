import requests

# Базовый URL API
BASE_URL = "https://api.pokemonbattle.ru/v2/"
HEADERS = {
    "Content-Type": "application/json",
    "trainer_token": "0d9066e7c4c132e5eb3cc79fc971bd6f"
}

# 1. Создание покемона (POST /pokemons)
def create_pokemon():
    url = BASE_URL + "pokemons"  # Формируем URL
    data = {
        "name": "generate",  # Используем "generate" для случайного имени
        "photo_id": -1
    }
    response = requests.post(url, headers=HEADERS, json=data)
    
    if response.status_code == 201:
        print("Создание покемона:")
        print(response.json())  # Выводим JSON-ответ
        return response.json().get("id")  # Возвращаем ID созданного покемона
    else:
        print("Ошибка при создании покемона:")
        print(response.json())
        return None



# 2. Смена имени покемона (PUT /pokemons)
def update_pokemon(pokemon_id):
    if not pokemon_id:
        print("ID покемона не предоставлен. Пропускаем смену имени.")
        return
    
    url = BASE_URL + "pokemons"  # Формируем URL
    data = {
        "pokemon_id": pokemon_id,
        "name": "generate",
        "photo_id": -1
    }
    response = requests.put(url, headers=HEADERS, json=data)
    
    if response.status_code == 200:
        print("\nСмена имени покемона:")
        print(response.json())  # Выводим JSON-ответ
    else:
        print("\nОшибка при смене имени покемона:")
        print(response.json())

# 3. Поймать покемона в покебол (POST /trainers/add_pokeball)
def catch_pokemon(pokemon_id):
    if not pokemon_id:
        print("ID покемона не предоставлен. Пропускаем попытку поймать покемона.")
        return
    
    url = BASE_URL + "trainers/add_pokeball"  # Формируем URL
    data = {
        "pokemon_id": str(pokemon_id)  # Преобразуем ID в строку, если это необходимо
    }
    response = requests.post(url, headers=HEADERS, json=data)
    
    if response.status_code == 200:
        print("\nПоймать покемона в покебол:")
        print(response.json())  # Выводим JSON-ответ
    else:
        print("\nОшибка при попытке поймать покемона:")
        print(response.json())


# Основная функция программы
if __name__ == "__main__":
    # Шаг 1: Создание покемона
    pokemon_id = create_pokemon()

    # Шаг 2: Смена имени покемона
    if pokemon_id:
        update_pokemon(pokemon_id)

    # Шаг 3: Поймать покемона в покебол
    if pokemon_id:
        catch_pokemon(pokemon_id)