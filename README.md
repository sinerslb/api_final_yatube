### Описание:
REST API проекта Yatube
### Установка:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/sinerslb/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

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
### Пример работы:
Запрос:

    GET  /api/v1/posts/:

Ответ:

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