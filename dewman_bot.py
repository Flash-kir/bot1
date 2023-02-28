import os

import argparse
import logging
import requests
import telegram
from dotenv import load_dotenv
from time import sleep


def get_checked_works(token, timestamp):
    url = 'https://dvmn.org/api/long_polling/'
    headers = {
        'Authorization': f'Token {token}',
    }
    params = {}
    if timestamp != 0:
        params['timestamp'] = timestamp
    response = requests.get(url, headers=headers, params=params, timeout=90)
    response.raise_for_status()
    return response.json()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-id',
        '--chat_id',
        default='Cosmos_pictures',
        help='chat_id telegram'
        )
    args = parser.parse_args()
    logger = logging.getLogger('bot')
    logger.setLevel(logging.ERROR)
    load_dotenv()
    dewman_token = os.environ.get('DEWMAN_TOKEN')
    telegram_bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')
    chat_id = f'@{args.chat_id}'
    bot = telegram.Bot(token=telegram_bot_token)
    timestamp = 0
    while True:
        try:
            response = get_checked_works(dewman_token, timestamp)
            if response['status'] == 'timeout':
                timestamp = response['timestamp_to_request']
                logger.debug(response['timestamp_to_request'])
            elif response['status'] == 'found':
                for lesson in response['new_attempts']:
                    lesson_status = 'Принята работа'
                    if lesson['is_negative']:
                        lesson_status = 'Возвращена на доработку работа'
                    lesson_title = lesson['lesson_title']
                    lesson_url = lesson['lesson_url']
                    bot.send_message(
                        chat_id=chat_id,
                        text=f'{lesson_status}: "{lesson_title}" ({lesson_url})'
                        )
                logger.debug('Проверенные работы: ', response)
        except requests.exceptions.HTTPError:
            logger.error('не удалось получить количество проверенных работ')
        except requests.exceptions.ReadTimeout:
            logger.error('не удалось получить ответ сервера')
        except requests.exceptions.ConnectionError:
            logger.error('нет связи с сервером')
            sleep(10)


if __name__ == '__main__':
    main()
