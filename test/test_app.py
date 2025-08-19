from app import app

def test_index():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Hello, Flask is working, Welcome to CI/CD Pipeline, DevOps!" in response.data

