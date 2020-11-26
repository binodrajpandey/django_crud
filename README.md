## Install Django
```
pip install django
python -m django --version
```
## Create a project
```
django-admin startproject django_project
```
## Run Project
```
python manage.py runserver
or
python manage.py runserver 8080
```
Now go to http://127.0.0.1:8000/admin

## Create super user
```
python manage.py makemigration
python manage.py migrate
python manage.py createsuperuser
```
