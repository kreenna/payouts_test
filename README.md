# Payout Request Test

Небольшой REST-сервис для управления заявками на выплату средств.

---

## Основные возможности
- CRUD API для заявок на выплату:
    - ```GET /api/payouts/```
    - ```GET /api/payouts/{id}/```
    - ```POST /api/payouts/```
    - ```PATCH /api/payouts/{id}/```
    - ```DELETE /api/payouts/{id}/```
- Асинхронная обработка заявок через Celery + Redis;
- Валидация полей (сумма, валюта, реквизиты получателя);
- Автоматически сгенерированная Swagger/OpenAPI-документация через drf-spectacular;
- Набор тестов для ViewSet (включая мок Celery-задачи);
- Docker/Docker Compose для запуска всего стека;
- CI-конфигурация (GitHub Actions) с тестами и линтерами.

---

## Локальный запуск без Docker

1. Клонировать репозиторий
```
git clone <URL_ВАШЕГО_РЕПОЗИТОРИЯ> payout-service
cd payout-service
```

2. Создать и активировать виртуальное окружение

```
python -m venv venv
source venv/bin/activate      # Linux/macOS
# или
venv\Scripts\activate         # Windows
```

3. Установить зависимости

```
pip install --upgrade pip
pip install -r requirements.txt
```

4. Настроить переменные окружения на основе .env-sample

5. Применить миграции

```
python manage.py migrate
```

6. Создать админа с помощью кастомной команды

```
python manage.py createadmin
```

8. Запустить Django dev-сервер

```
python manage.py runserver
```

---

## Запуск Docker

1. Клонируйте репозиторий:

```
git clone https://github.com/kreenna/payouts_test
cd payouts_test
```

2. Создайте файл .env с переменными окружения на основе .env-sample.

3. Запустите Docker-контейнеры:

```
docker-compose up --build
```

4. При первом запуске выполнится миграция, сбор статики и команда createadmin, которая создаст администратора:

```
username: admin
password: 123qwe456rty
```

---