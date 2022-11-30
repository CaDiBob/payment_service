### Тестовое задание:
Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:

Django Модель Item с полями (name, description, price)

API с двумя методами:

GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id) Пример реализации можно посмотреть в пунктах 1-3 тут
Залить решение на Github, описать запуск в Readme.md


Использование environment variables

Просмотр Django Моделей в Django Admin панели

Запуск приложения на удаленном сервере, доступном для тестирования

### Запуск

Склонируйте репозиторий

```bash
git clone git@github.com:CaDiBob/payment_service.git
```
Перейдите в папку с проектом

```bash
cd payment_service/
```

Python должен быть установлен, затем используйте pip:

```bash
pip install -r requirements.txt
```

#### Переменные окружения

Заполните переменные окружения в файле `.env`:
`ALLOWED_HOSTS` - Разрешенные хосты. Указываются через запятую, например: `127.0.0.1,localhost`.
`SECRET_KEY` - Секретный ключ.
`DEBUG` - Если нужно включить режим отладки web-сервера, установите значение в `True`.
`STRIPE_API_KEY` - Секретный ключ от [API Stripe](https://dashboard.stripe.com/apikeys/).
`DATABASE_URL` - Django database url postgres://имя пользователя:пароль@хост:порт(5432)/имя базы данных

#### Для локальной разработки

```bash
./manage.py createsuperuser
```

```bash
./manage.py runserver
```

Тестовый сервер будет доступен по http://127.0.0.1:8000/

#### Запуск с docker-compose

```bash
sudo docker-compose up -d --build
```

#### Демо сервер

доступен по адресу http://89.208.106.153/

##### Админка

http://89.208.106.153/admin

`логин` - root

`пароль` - admin

##### Домашняя страница со списком товаров для тестирования

http://89.208.106.153/

##### Страница товара

http://89.208.106.153/item/id_товара
