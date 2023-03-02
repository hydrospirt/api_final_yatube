# API YATUBE
Это открытый API. Читай, публикуй, подписывайся на понравившихся авторов. А так же вступай в группы по интересам. Уже сейчас функция добавления картинок к публикациям.
### Технологии проекта:
* Python 3.9
* Django / Django Rest Framework
* Sqlite
* ReDoc

### Примеры запросов:
**Получение публикаций**
Получить список всех публикаций. При указании параметров limit и offset выдача работает с пагинацией.
GET запрос:
```
http://127.0.0.1:8000/api/v1/posts/?offset=300&limit=100
```
Response 200:
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

**Подписка**
Подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса. Анонимные запросы запрещены.
POST запрос:
```
http://127.0.0.1:8000/api/v1/follow/
```
Response 200:
```
{
  "user": "string",
  "following": "string"
}
```
**Добавление комментария**
Добавление нового комментария к публикации. Анонимные запросы запрещены.
POST-запрос:
```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```
Payload:
```
{
  "text": "string"
}
```
Response 200:
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```
## Получить JWT-токен
Получение JWT-токена. Только для POST-запросов
```
http://127.0.0.1:8000/api/v1/jwt/create/
```
Payload:
```
{
  "username": "string",
  "password": "string"
}
```
Response 200:
```
{
  "refresh": "string",
  "access": "string"
}
```

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git@github.com:hydrospirt/api_yatube.git
```

```
cd yatube_api
```

Cоздать и активировать виртуальное окружение:

```
py -3.9 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```
Обновить pip
```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Разработчики

| Имя | Ссылка |
| ------ | ------ |
| Eduard Human | https://github.com/hydrospirt