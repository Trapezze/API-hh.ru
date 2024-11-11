import requests

# Функция для получения токена доступа
def get_access_token(client_id, client_secret):
    url = "https://hh.ru/oauth/token"
    data = {
        "grant_type": "client_credentials",  # исправлено: было "client_credietials"
        "client_id": client_id,
        "client_secret": client_secret
    }

    response = requests.post(url, data=data)
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        print("Ошибка при получении токена:", response.status_code, response.text)
        return None

# Функция для поиска вакансий
def search_vacancies(keyword, access_token, area=1, page=0, per_page=10):
    url = "https://api.hh.ru/vacancies"  # исправлено: было "irl"
    headers = {
        "Authorization": f"Bearer {access_token}"  # исправлено: было "Autorization"
    }
    params = {
        "text": keyword,
        "area": area,
        "page": page,
        "per_page": per_page  # исправлено: было "per+page"
    }

    response = requests.get(url, headers=headers, params=params)  # исправлено: было "respons"
    if response.status_code == 200:
        return response.json().get('items', [])
    else:
        print("Ошибка при запросе:", response.status_code, response.text)
        return []

# Основной код
client_id = "Ваш ckient_id"
client_secret = "Ваш client_secre"

# Получение токена доступа
access_token = get_access_token(client_id, client_secret)
if access_token:
    # Поиск вакансий по ключевому слову "Python разработчик"
    vacancies = search_vacancies("Python разработчик", access_token)

    # Вывод информации о вакансиях
    for vacancy in vacancies:
        print(f"Название: {vacancy['name']}")
        print(f"Компания: {vacancy['employer']['name']}")
        print(f"Зарплата: {vacancy['salary']}")
        print(f"Ссылка: {vacancy['alternate_url']}\n")
