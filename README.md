Запуск на локальном сервере:
1. mkdir hr
2. cd hr
3. git init
4. git pull https://github.com/riderufa/ProjectHR
5. python3 -m venv venv
6. source venv/bin/activate
7. pip install -r requirements.txt
8. docker run --name django-db -e POSTGRES_PASSWORD=docker -d -p 5432:5432 postgres:12-alpine 
9. docker exec -it django-db psql -U postgres -c "create database poll_db"
10. docker run --name redis-instance -d -p 6379:6379 redis:5.0.7 redis-server --appendonly yes
11. python manage.py migrate
12. python manage.py createsuperuser
13. python manage.py runserver

Стек технологий:
1. Django
2. Postgres
3. Redis
4. Bootstrap
5. Gunicorn
6. Whitenoise