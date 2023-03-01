# API YATUBE


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
