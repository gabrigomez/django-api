import requests

ENDPOINT = "https://todo.pixegami.io"
LOCAL_ENDPOINT = "http://127.0.0.1:8000"


def test_call_api():
    response = requests.get(LOCAL_ENDPOINT + '/user')
    assert response.status_code == 200

def test_can_create_task():
    payload = {
        "content": "my test",
        "user_id": "mocoto",
        "task_id": "test_id_666",
        "is_done": "false",
    }
    response = requests.put(ENDPOINT + "/create-task", json=payload)
    assert response.status_code == 200

    data = response.json()
    print(data)