import requests


def generate_joke() -> str:
    url = 'https://icanhazdadjoke.com/'
    headers = {'Accept': 'text/plain'}

    response = requests.get(url, headers=headers)

    return response.text


if __name__ == '__main__':
    print(generate_joke())
