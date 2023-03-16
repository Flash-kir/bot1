import os

import argparse
import logging
import requests
import telegram
from dotenv import load_dotenv
from time import sleep, time


class MyLogsHandler(logging.Handler):

    def emit(self, record):
        log_entry = self.format(record)
        bot.send_message(
            chat_id=args.user_id,
            text=f'{log_entry}'
        )


logger = logging.getLogger('bot')


def main():
    timestamp = time()
    while True:
        try:
            headers = {
                'Authorization': f'Token {devman_token}',
            }
            params = {
                'timestamp': timestamp
            }
            response = requests.get(
                'https://dvmn.org/api/long_polling/',
                headers=headers,
                params=params,
                timeout=90
                )
            response.raise_for_status()
            works = response.json()
            if works['status'] == 'timeout':
                timestamp = works['timestamp_to_request']
                logger.debug(works['timestamp_to_request'])
            elif works['status'] == 'found':
                for work in works['new_attempts']:
                    timestamp = work['timestamp']
                    work_status = 'Принята работа'
                    if work['is_negative']:
                        work_status = 'Возвращена на доработку работа'
                    work_title = work['lesson_title']
                    work_url = work['lesson_url']
                    bot.send_message(
                        chat_id=args.user_id,
                        text=f'{work_status}: "{work_title}" ({work_url})'
                        )
                logger.debug('Проверенные работы: ', works)
        except requests.exceptions.HTTPError:
            logger.error('не удалось получить количество проверенных работ')
        except requests.exceptions.ReadTimeout:
            logger.error('не удалось получить ответ сервера')
        except requests.exceptions.ConnectionError:
            logger.error('нет связи с сервером')
            sleep(10)
        except Exception as err:
            logger.error(err, exc_info=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-id',
        '--user_id',
        default='199351989',
        help='user id telegram'
        )
    args = parser.parse_args()
    logging.basicConfig(format="%(levelname)s[%(asctime)s]: %(message)s(%(pathname)s: %(funcName)s - line %(lineno)d)")
    logger.setLevel(logging.ERROR)
    load_dotenv()
    devman_token = os.environ.get('DEVMAN_TOKEN')
    telegram_bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')
    bot = telegram.Bot(token=telegram_bot_token)
    handler = MyLogsHandler()
    logger.addHandler(handler)
    main()
