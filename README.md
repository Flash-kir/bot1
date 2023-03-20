## devman_bot.py

Программа отправляет запрос на адрес `https://dvmn.org/api/long_polling/` для проверки статуса выполненных работ пользователя.
Бот отправит уведомление вида `Возвращена на доработку работа: "Отправляем уведомления о проверке работ" (https://dvmn.org/modules/chat-bots/lesson/devman-bot/)` если работа проверена.

## Установка и запуск

Клонируйте реппозиторий:

```bash
    git clone git@github.com:Flash-kir/bot1.git
```

Выполните команду:

```bash
$ pip install -r requirenments.txt
```

У кажите токены Devman, бота telegram и Chat id телеграмм в файле .env, предварительно выполнив команду:

```bash
$ cp example.env .env
```

Запустите программу командой:

```bash
$ python devman_bot.py
```

## Установка и запуск с использованием Docker

Клонируйте реппозиторий:

```bash
$ git clone git@github.com:Flash-kir/bot1.git
```

Установите [Docker](https://docs.docker.com/engine/install/)

### Создание образа и запуск локально

Создайте образ, выполнив команду(команда выполняется в папке с файлом `devman_bot.py`):

```bash
$ docker build -t chat-bot .
```

Запустите его(команда выполняется в папке с файлом `devman_bot.py`):

```bash
$ docker run -d --env-file .env chat-bot
```

### Клонирование и запуск образа на сервере

Клонируйте образ командой:

```bash
$ docker pull flashkir/chat-bot
```

Запустите его

```bash
$ /usr/bin/docker run -d --env-file {Полный путь до .env файла}.env flashkir/chat-bot
```

