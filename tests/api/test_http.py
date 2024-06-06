import pytest
import requests


@pytest.mark.http
def test_first_requests():
    r = requests.get('https://api.github.com/zen')
    print(r.text)


@pytest.mark.http
def test_second_requests():
    r = requests.get('https://api.github.com/users/krokhavolpe')
    body = r.json()
    headers = r.headers

    assert body['login'] == 'KrokhaVolpe'
    assert r.status_code == 200
    assert headers['Server'] == 'GitHub.com'


@pytest.mark.http
def test_second_requests():
    r = requests.get('https://api.github.com/users/krokhavolpee')
    assert r.status_code == 404
