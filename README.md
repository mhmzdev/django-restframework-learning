## Django-restframework learning

I've put all the files in sequence in the branches while I'm learning to use django as backend framework.

### 1st - Creating Django project
- Created django project using command `django-admin startproject learning`

### 2nd - First API view/response
- Created first api view, or we also call it api response
- Create app name `api` via command `python manage.py startapp api`
- return json response from url `http://localhost:8000/home/`

### 3rd - Returning back Data
- Sending Json data from client side to server and handling it.
- More like we send `body` in a `POST` request or `QueryParams`
- Adding data like `headers` and `content_type`