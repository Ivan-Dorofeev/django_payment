# django_payment

Реализация оплаты любого товара через библиотеку Stripe

## Запуск

- Сначала необходимо зайти на сайт [Stripe](https://dashboard.stripe.com/products/) и создать свой аккаунт.
Там же создать ссылки для оплаты на каждую сумму (подробнее тут: [Документация Stripe](https://stripe.com/docs/payments/online-payments))

 - Для запуска сайта вам понадобится Python третьей версии.

- Скачайте код с GitHub. Установите зависимости:

    ```sh
    pip install -r requirements.txt
    ```

 - Создайте базу данных SQLite

    ```sh
    python3 manage.py makemigrations
    ```
    ```sh
    python3 manage.py migrate
    ```
 - Запустите разработческий сервер
    
    ```
    python3 manage.py runserver
    ```

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `SECRET_DJANGO_KEY` — секретный ключ приложения Django
- `STRIPE_PUBLISHABLE_KEY` — публичный ключ Stripe
- `STRIPE_SECRET_KEY` — секретный ключ Stripe
