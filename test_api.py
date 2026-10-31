import requests
BASE_URL = "http://127.0.0.1:8000"
def test_health():
    response = requests.get(BASE_URL + "/health", timeout=10)
    assert response.status_code == 200, (
            f"Expected status 200, got {response.status_code}"
        )
    data = response.json()
    assert data["status"] == "healthy",(
        f"Expected status 'healthy', got {data['status']}"
    )

def test_home():
    response = requests.get(BASE_URL + "/", timeout=10)

    assert response.status_code == 200, (
        f"Expected status 200, got {response.status_code}"
    )

    data = response.json()

    assert data["message"] == "Welcome to my work", (
        f"Unexpected message: {data.get('message')}"
    )
def test_predict_positive(): 
    text = "I love this test" 
    response = requests.post(BASE_URL + "/predict", json={"text": text}, timeout=10)
    assert response.status_code == 200, (
        f"Expected status 200, got {response.status_code}"
    )
    data = response.json() 
    assert data["sentiment"] == "POSITIVE", (
        f"Expected sentiment 'POSITIVE', got {data['sentiment']}")
def test_predict_negative(): 
    text = "I hate this test" 
    response = requests.post(BASE_URL + "/predict", json={"text": text}, timeout=10)
    assert response.status_code == 200, (
        f"Expected status 200, got {response.status_code}"
    )
    data = response.json() 
    assert data["sentiment"] == "NEGATIVE", (
        f"Expected sentiment 'NEGATIVE', got {data['sentiment']}")
def test_empty_text():
    text = "     "
    response = requests.post(BASE_URL + "/predict", json={"text": text}, timeout=10)
    assert response.status_code == 400, (
        f"Expected status 400, got {response.status_code}"
    )
    data = response.json()
    assert data["detail"] == "Text cannot be empty", (
        f"Expected detail 'Text cannot be empty', got {data['detail']}"
    )