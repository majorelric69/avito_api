import configuration
import requests
import data

#Создание объявления для пользователя с заполненными корректно обязательными полями
def test_create_announce_correct():
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ANNOUNCE,
                         json=data.correctbody)
    assert response.status_code == 201

#Создание объявления для пользователя с заполненными некорректно обязательными полями
def test_create_announce_incorrect():
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ANNOUNCE,
                         json=data.incorrectbody)
    assert response.status_code == 400

#Получение  всех объявлений  по существующему идентификатору продавца
def test_existing_user():
    response = requests.get(configuration.URL_SERVICE + configuration.GET_ALL_ANNOUNCE,
                 params={"sellerID": data.exist_user_value})
    assert response.status_code == 200

#Получение  всех объявлений  по несуществующему идентификатору продавца
def test_not_existing_user():
    response = requests.get(configuration.URL_SERVICE + configuration.GET_ALL_ANNOUNCE,
                 params={"sellerID": data.not_exist_user_value})
    assert response.status_code == 400

#Получение объявления по существующему идентификатору
def test_existing_announce():
    response = requests.get(configuration.URL_SERVICE + configuration.GET_ANNOUNCE_ID +data.announce_exist_id)
    assert response.status_code == 200

#Получение объявления по несуществующему идентификатору
def test_not_existing_announce():
    response = requests.get(configuration.URL_SERVICE + configuration.GET_ANNOUNCE_ID +data.announce_not_exist_id)
    assert response.status_code == 404

#Получение объявления по нулевому идентификатору
def test_null_announce():
    response = requests.get(configuration.URL_SERVICE + configuration.GET_ANNOUNCE_ID +data.announce_null)
    assert response.status_code == 404