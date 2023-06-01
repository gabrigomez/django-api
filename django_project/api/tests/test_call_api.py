import requests
import random
import string

ENDPOINT = "https://todo.pixegami.io"
LOCAL_ENDPOINT = "http://127.0.0.1:8000"

def random_name(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

def test_call_api():
    response = requests.get(LOCAL_ENDPOINT + '/user')
    assert response.status_code == 200

def test_can_post_user():
    range_number = random.randint(3,12)
    email = random_name(range_number).lower()
    username = random_name(range_number)
    
    payload = {
        "email": f"{email}@gmail.com",
        "username": f"{username}",
        "password": "askovzinha123"
    }
    response = requests.post(LOCAL_ENDPOINT + "/create-user", json=payload)
    assert response.status_code == 201

    data = response.json()
    print(data)

def test_can_find_user():
    response = requests.get(LOCAL_ENDPOINT + '/user/9')
    assert response.status_code == 200

def test_can_delete_user():
    response = requests.delete(LOCAL_ENDPOINT + '/user/1')
    assert response.status_code == 201

    response = requests.get(LOCAL_ENDPOINT + '/user/1')
    assert response.status_code == 404

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