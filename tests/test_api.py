import sys
import os

# Add the project root directory to sys.path so 'app' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_api_response():
    from app.main import app
    with app.test_client() as client:
        res = client.post('/', data={"text": "Oh great, another Monday"})
        assert res.status_code == 200
