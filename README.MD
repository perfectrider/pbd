1. Для запуска приложения необходимо создать `.env` файл с переменными окружения:

```python
SECRET_KEY=django-insecure-y2k63vcovt2jujc#4c=s6aa3&b7d*0cji!4!p0u*101g1bd85@

DB_NAME={имя вашей бд}
DB_USER={имя пользователя бд}
DB_PASSWORD={пароль бд}
DB_HOST=0.0.0.0
DB_PORT=5432
```

2. Для запуска БД в контейнере выполнить
```python
docker compose up
```
...или не указать в `.env` файле параметры для подключения к вашей локальной БД.


2. Далее выполнить миграции:

```python
python3 manage.py makemigrations
python3 manage.py migrate
```

3. Запустить сервер:

```python
python3 manage.py runserver
```