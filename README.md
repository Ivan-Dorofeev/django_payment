# django_payment

Реализация оплаты любого товара через библиотеку Stripe

![image](https://user-images.githubusercontent.com/58893102/203936956-aaff6b0e-668c-47dd-b76d-f5ecc030738d.png)

## Описание

В БД уже есть несколько товаров для теста.
Заходим на главную сраницу --> выбираем товар --> нажимаем на кнопку "BUY":

![image](https://user-images.githubusercontent.com/58893102/203937437-9e9500f8-1a31-455d-8e93-c0c6ad415f72.png)

Получаем ссылку на оплату, переходим по ней.

## Запуск

Для запуска сайта вам понадобится Python третьей версии.

Скачайте код с GitHub. Установите зависимости:

```sh
pip install -r requirements.txt
```

Создайте базу данных SQLite

```sh
python3 manage.py makemigrations
```
```sh
python3 manage.py migrate
```
Запустите разработческий сервер

```
python3 manage.py runserver
```

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `SECRET_DJANGO_KEY` — секретный ключ приложения Django
- `STRIPE_PUBLISHABLE_KEY` — публичный ключ Stripe
- `STRIPE_SECRET_KEY` — секретный ключ Stripe
