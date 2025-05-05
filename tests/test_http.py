import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(f"Response is {r.text}")

@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    body = r.json()
    headers = r.headers

    assert body['name'] == 'Chris Wanstrath'
    assert r.status_code == 200
    assert headers['Server'].lower() == 'github.com'


@pytest.mark.http
def test_status_code_request():
    r = requests.get('https://api.github.com/users/sergii_butenko')

    assert r.status_code == 404


@pytest.mark.http
def test_first_request():
    response = requests.get("https://api.github.com/zen")
    print(f"Відповідь від сервера: {response.text}")
    assert response.status_code == 200  # базова перевірка

@pytest.mark.http
def test_second_request():
    response = requests.get("https://api.github.com/users/defunkt")
    json_data = response.json()

    assert response.status_code == 200
    assert json_data["name"] == "Chris Wanstrath"
    assert response.headers["Server"] == "GitHub.com"

@pytest.mark.http
def test_status_code_request():
    response = requests.get("https://api.github.com/users/sergii_butenko")
    assert response.status_code == 404
