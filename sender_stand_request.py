# Импорт модуля configuration, который содержит настройки подключения и путь к документации
import configuration
# Импорт модуля requests, предназначенный для отправки HTTP-запросов и взаимодействия с веб-сервисами
import requests 
# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data 


        ### 1-я функция создания нового пользователя

# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
# json=body используется для отправки данных пользователя в формате JSON
# headers=data.headers устанавливает заголовки запроса из модуля data
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

# Вызов функции post_new_user с телом запроса для создания нового пользователя из модуля data
response = post_new_user(data.user_body)

# Вывод полученного тела ответа в формате JSON в консоль для наглядности.
#print(response.json())

# Вывод HTTP-статус кода ответа на запрос
#print(response.status_code)

# Определение переменной, содержащий токен auth_token пользователя из функции Создания Пользователя
auth_token = response.json()["authToken"]

# Вывод токена пользователя для наглядности
#print(auth_token)


        ### 2-я функция для получения данных из таблицы пользователей

# Определение функции get_users_table для отправки GET-запроса на получение данных из таблицы пользователей
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)


# Определение хедера для POST-запроса на создание нового пользователя\
# Копирование хедера из data и сохранение в отдельную переменную\
# С токеном пользователя из функции Создания Пользователя
header_kit = data.headers.copy()
header_kit["Authorization"] = "Bearer "+auth_token
#print(header_kit)


        ### 3-я функция для создания нового набора от имени пользователя (auth_token)

# Определение функции post_new_user_kit для отправки POST-запроса на создание нового набора от имени пользователя
# json=body используется для отправки данных пользователя в формате JSON
# headers=header_kit устанавливает заголовок запроса с auth_token из функции создания нового пользователя
def post_new_user_kit(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_PRODUCTS_KITS_PATH,
                         json=body,
                         headers=header_kit)


        ### 4-я функция для получения данных из таблицы наборов

# Определение функции get_kit_table для отправки GET-запроса на получение данных из таблицы наборов
def get_kit_table():
    return requests.get(configuration.URL_SERVICE + configuration.KIT_TABLE_PATH)


