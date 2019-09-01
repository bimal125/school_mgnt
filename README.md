# Minimal School Management System

This backend system allows list, create, retrive, insert, update, partial update, delete features for school and students. There is one to many relationship between school and students. Each school has its maximum limit, system does not allow to create students if maximum limit reached. System allows to list, create, update, delete, retrive, partial update students belongs to school. Some features like filter, pagination, search, order by id implemented in both school and students. 

## Getting Started

Clone this repo. Install all packages in requirements.txt using,

Goto project root directory

Activate virtual environment

```
pipenv shell

```
Install dependencies

```
pipenv install or pipenv install --dev
```
To run tests

```
py.test
```

Copy .env.example file located inside school_mgnt/school_mgnt to .env and set  postgresql database credentials

```
cp school_mgnt/.env.example school_mgnt/.env 
```
Edit .env with your favorite editor

```
vi .school_mgnt/env
```
Run db migration

```
python manage.py migrate
```
Run djano server

```
python manage.py runserver
```