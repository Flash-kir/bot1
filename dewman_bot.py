import os
import requests
from dotenv import load_dotenv


def get_checked_works(token):
    url = 'https://dvmn.org/api/user_reviews/'
    headers = {
        'Authorization': f'Token {token}',
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def main():
    load_dotenv()
    dewman_token = os.environ.get('DEWMAN_TOKEN')
    try:
        print('Проверенные работы: ', get_checked_works(dewman_token))
    except requests.exceptions.HTTPError:
        print('не удалось получить количество проверенных работ')


if __name__ == '__main__':
    main()
