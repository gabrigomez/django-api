import requests

ENDPOINT = "https://todo.pixegami.io"

def test_call_api():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200