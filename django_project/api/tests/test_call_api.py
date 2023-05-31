import requests

ENDPOINT = "https://todo.pixegami.io"

def test_call_api():
    response = requests.get(ENDPOINT)
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