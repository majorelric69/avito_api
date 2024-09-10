Баг-репорты

Avito-1 Бэкенд создает новое объявление при указании пользователя с незаполненными обязательными полями, ручка POST https://qa-internship.avito.com/api/1/item
Шаги воспроизведения:
1. В ручке ввести https://qa-internship.avito.com/api/1/item, метод POST
2. В body ввести 
    {
        "name": "Телефон",
        "sellerId": 222222,
        "statistics": {
            "contacts": 32,
            "like": 35,
            "viewCount": 14
        }
    }
3. Нажать на Send
Ожидаемый результат: Объявление не создано, код 400
Фактический результат: Объявление создано, код 200
Окружение: Postman for Windows,v11.11.1, ОС Windows 10 Pro
<img src="\img\incorrect_post.png">

Avito-2 Статус код при создании запроса с корректными данными 200, ручка POST https://qa-internship.avito.com/api/1/item
Шаги воспроизведения:
1. В ручке ввести https://qa-internship.avito.com/api/1/item, метод POST
2. В body ввести 
    {
        "name": "Телефон",
        "price": 85566,
        "sellerId": 222222,
        "statistics": {
            "contacts": 32,
            "like": 35,
            "viewCount": 14
        }
    }
3. Нажать на Send
Ожидаемый результат: Объявление создано, код 201
Фактический результат: Объявление создано, код 200
Окружение: Postman for Windows,v11.11.1, ОС Windows 10 Pro
<img src="\img\correct_post.png">

Avito-3 При некорректном SellerID бэкенд показывает список объявлений пользователя с нулевым SellerID, ручка https://qa-internship.avito.com/api/1/:sellerID/item, метод GET
Шаги воспроизведения:
1. В ручке ввести https://qa-internship.avito.com/api/1/:sellerID/item, метод GET
2. В Params, Path Variables, Value ввести 111111111111111111111111111111111
3. Нажать на Send
Ожидаемый результат: Объявления не выведены, код 400
Фактический результат: Объявление создано, код 200
Окружение: Postman for Windows,v11.11.1, ОС Windows 10 Pro
<img src="\img\not_exist_user.png">

