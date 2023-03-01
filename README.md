## devman_bot.py

Программа принимает на вход аргумент:

  -id USER_ID, --user_id USER_ID user_id telegram для отправки уведомлений

Затем отправляется запрос на адрес `https://dvmn.org/api/long_polling/` для проверки статуса выполненных работ пользователя.
Бот отправит уведомление вида `Возвращена на доработку работа: "Отправляем уведомления о проверке работ" (https://dvmn.org/modules/chat-bots/lesson/devman-bot/)` если работа проверена.

## Установка и запуск

Клонируйте реппозиторий:

    git clone git@github.com:Flash-kir/bot1.git

Выполните команду:

    pip install -r requirenments.txt

У кажите токены Devman и бота telegram в файле .env, предварительно выполнив команду:

    cp example.env .env

Запустите программу командой:

    python devman_bot.py -id id_пользователя

