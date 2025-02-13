# Импорт модуля sender_stand_request, содержащий функции для отправки HTTP-запросов к API
import sender_stand_request
# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data


# Шаг 1. Тест запроса на создание пользователя c исходными данными data

# Определение функции test_create_new_user для отправки POST-запроса на создание нового пользователя
def test_create_new_user():
    user_response = sender_stand_request.post_new_user(data.user_body)
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""
    users_table_response = sender_stand_request.get_users_table()
    str_user = data.user_body["firstName"] + "," + data.user_body["phone"] + "," \
               + data.user_body["address"] + ",,," + user_response.json()["authToken"]
    assert users_table_response.text.count(str_user) == 1


# Шаг 2. Тест запроса на создание личного набора для пользователя c исходными данными data

# Определение функции test_create_new_kit для отправки POST-запроса на создание нового набора
def test_create_new_kit():
    kit_response = sender_stand_request.post_new_user_kit(data.products_kit_body)
    # Проверка соответствия кода ответа, тела ответа, токена пользователя
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == data.products_kit_body["name"]
    assert kit_response.json()["productsList"] == None
    assert kit_response.json()["productsCount"] == 0
    assert kit_response.json()["id"] !=""


# Шаг 3. Функция заменяет значения в параметре name

def get_kit_body(name):
    current_body = data.products_kit_body.copy()
    current_body["name"] = name
    return current_body


# Шаг 4. Запрос на создание личного набора для нового пользователя c новыми данными

# Определение функции test_create_new_client_kit для отправки POST-запроса на создание нового пользовательского набора
def test_create_new_client_kit():
    kit_body = get_kit_body("а")
    kit_responce = sender_stand_request.post_new_user_kit(kit_body)
    # Проверка соответствия кода ответа, тела ответа, токена пользователя
    assert kit_responce.status_code == 201
    assert kit_responce.json()["productsList"] == None
    assert kit_responce.json()["productsCount"] == 0
    assert kit_responce.json()["id"] !=""



# Шаг 5. Определение функции для позитивной проверки

def positive_assert(name):
    kit_body = get_kit_body(name)
    kit_responce = sender_stand_request.post_new_user_kit(kit_body)
    # Проверка соответствия ответа
    assert kit_responce.status_code == 201
    assert kit_responce.json()["productsList"] == None
    assert kit_responce.json()["productsCount"] == 0
    assert kit_responce.json()["id"] !=""


# Шаг 6. Определение функции для негативной проверки

def negative_assert_code_400(name):
    # В переменную user_body сохраняется обновлённое тело запроса
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_user_kit(kit_body)
    assert kit_response.status_code == 400
    

# Шаг 7. Автотесты

# Автотест 1 - Допустимое количество символов (1)
def test_create_userkit_1_letter_get_succes_responce():
    positive_assert("а")

# Автотест 2 - Допустимое количество символов (511)
def test_create_userkit_511_letter_get_succes_responce():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
                    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
                    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbc\
                    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
                    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
                    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
                    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
                    bcdabcdabcdabcdabcdabcdabC")

# Автотест 3 - Количество символов меньше допустимого (0)
def test_create_userkit_0_letter_get_failure_responce():
    negative_assert_code_400("") 

# Автотест 4 - Количество символов больше допустимого (512)
def test_create_userkit_512_letter_get_failure_responce():
    negative_assert_code_400("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
                    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
                    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbc\
                    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
                    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
                    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
                    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
                    bcdabcdabcdabcdabcdabcdabcD")  

# Автотест 5 - Разрешены английские буквы
def test_create_userkit_ENG_letter_get_succes_responce():
    positive_assert("QWErty")

# Автотест 6 - Разрешены русские буквы
def test_create_userkit_RUS_letter_get_succes_responce():
    positive_assert("Мария")

# Автотест 7 - Разрешены спецсимволы
def test_create_userkit_SYMBOLS_get_succes_responce():
    positive_assert('"№%@",')

# Автотест 8 - Разрешены пробелы
def test_create_userkit_SPACES_get_succes_responce():
    positive_assert("Человек и КО")

# Автотест 9 - Разрешены цифры
def test_create_userkit_NUMB_letter_get_succes_responce():
    positive_assert("123")

# Автотест 10 - Параметр не передан в запросе
def test_create_userkit_0_letter_get_failure_responce():
    negative_assert_code_400(None) 

# Автотест 11 - Передан другой тип параметра (число)
def test_create_userkit_integer_get_failure_responce():
    negative_assert_code_400(123) 
