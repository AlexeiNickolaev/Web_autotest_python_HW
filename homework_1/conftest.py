import pytest
import yaml
import requests


with open('config.yaml') as f:
    conf = yaml.safe_load(f)


@pytest.fixture()
def login():
    obj_data = requests.post(url=conf['url'], data={
                             'username': 'Smol123', 'password': 'f0976457a2'})
    token = obj_data.json()['token']
    return token


@pytest.fixture()
def post():
    obj_data = requests.post(url=conf['url1'], headers={"X-Auth-Token": conf['token']}, data={
        'username': 'Smol123',
        'password': 'f0976457a2',
        'title': 'newTitle',
        'description': 'Hello, World!',
        'content': 'Hello content'})
    return obj_data.json()['description']
