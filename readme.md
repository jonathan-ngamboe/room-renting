# G09 GPTEAM ✌️ 🐍

## Application Logo
<img src="https://freelogopng.com/images/all_img/1681038325chatgpt-logo-transparent.png" alt="GPTeam" title="GPTeam" width="200"/>

## Introduction
### Description
The Room Renting application is designed for students planning to spend time at another HES-SO institution. It aims to facilitate finding accommodation for these students or renting out their rooms or apartments when they are not needed temporarily. Additionally, it allows those with available rooms or apartments to easily find suitable tenants.

## Diagrams

### Class diagramm
![Class diagramm](/media/readme/GPTeam_Interschool.png "Class diagramm")

### System Architecture 

```mermaid
graph TD;
    A[User] --> B[Frontend - Vue.Js/Quasar];
    B --> C[Backend - Node.js];
    C --> D[(Database - Django/SQlite3)];
```

## Technologies
- **Frontend**: Vue.js / Version 3.4.27
- **Frontend**: Quasar framework / Version 1.16.11
- **Backend**: Node.js / Version v20.11.1
- **Database**: Django with Sqlite3 / Version 5.0.4


Vue and Django are clearly separated in this project. Vue, npm and Webpack handles all frontend logic and bundling assessments. Django and Django REST framework to manage Data Models, Web API and serve static files.

While it's possible to add endpoints to serve django-rendered html responses, the intention is to use Django primarily for the backend, and have view rendering and routing and handled by Vue + Vue Router as a Single Page Application (SPA).

Out of the box, Django will serve the application entry point (`index.html` + bundled assets) at `/` ,
data at `/api/`, and static files at `/static/`. Django admin panel is also available at `/api/admin/` and can be extended as needed.

The application templates from Vue CLI `create` and Django `createproject` are kept as close as possible to their
original state, except where a different configuration is needed for better integration of the two frameworks.

### Authentication
Sample register, login, logout function are implemented in the client.
More endpoints options are available in the backend,
see [dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/api_endpoints.html).

### Includes

* Django
* Django REST framework
* Django CORS Headers
* Django Whitenoise
* login via JWT using dj-rest-auth
* Vue 3 Vite
* Vue Router
* Gunicorn


### Template Structure


| Location             |  Content                                   |
|----------------------|--------------------------------------------|
| `/backend`           | Django Project & Backend Config            |
| `/backend/api`       | Django App (`/api`)                        |
| `/media`             | Images                                     |
| `/src`               | Vue App .                                  |
| `/src/main.js`       | JS Application Entry Point                 |
| `/src/assets/css`    | CSS of the application                     |
| `/src/components`    | Components used on the Frontend            |
| `/src/layouts`       | Layout used on all the application         |
| `/src/router`        | Redirection of the different pages         |
| `/src/services`      | Methods to communicate with DATABASE       |
| `/src/utils`         | Methods used on different views            |
| `/src/views`         | Views of the different pages               |
| `/index.html`        | [Html Application Entry Point](https://cli.vuejs.org/guide/html-and-static-assets.html) (`/`)         |
| `/public`            | favicon                                    |


## Prerequisites

Before getting started you should have the following installed and running:

- [X] Node - [instructions](https://nodejs.org/en/)
- [X] Vue 3 - [instructions](https://vuejs.org/)
- [X] Vite - [instructions](https://vitejs.dev/)
- [X] Python 3 - [instructions](https://wiki.python.org/moin/BeginnersGuide)

## Setup Template

Setup frontend
```
$ npm install
```

Setup backend
```
$ python -m venv venv
```
```
# On windows
$ .\venv\Scripts\Activate.ps1

# On linux
$ source venv/bin/activate
```
```
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py loaddata .\backend\api\fixtures\initial_data.json
$ python manage.py createsuperuser --email admin@example.com --username admin
```

## Running Development Servers

Frontend

```
$ npm run dev
```
From another tab in the same directory:

Backend

```
$ python manage.py runserver
```


The Vue application will be served from [`localhost:5173`](http://localhost:5173/) and the Django API
and static files will be served from [`localhost:8000`](http://localhost:8000/).

The dual dev server setup allows you to take advantage of
vite's development server with hot module replacement.

This requires cors to be configured correctly in Django.

```
CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:8080",
    "http://127.0.0.1:9000",
]
```

## urls
http://localhost:5173/#/ for vue frontend
http://localhost:8000/api/ for django rest framework api
http://localhost:8000/api/admin/ for django admin



## Deploy

For production you need to change **baseURL** in `src/services/api.js` 

### Production deployment
env variables to configure
```
DATABASE_URL
DJANGO_DEBUG
DJANGO_SECRET_KEY
DJANGO_ALLOWED_HOSTS
DJANGO_SETTINGS_MODULE=backend.settings.prod
```

## Static Assets

See [`vite.config.js`](/vite.config.js) for notes on static assets strategy.

This template implements the approach suggested by Whitenoise Django.
For more details see [WhiteNoise Documentation](http://whitenoise.evans.io/en/stable/django.html)

It uses Django Whitenoise to serve all static files and Vue bundled files at `/static/`.

## Authors
* Léticia Tscherrig
* Francesco De Fino
* David Bürki
* Jonathan Ngamboe
