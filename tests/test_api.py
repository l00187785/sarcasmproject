def test_api_response():
    from app.main import app
    with app.test_client() as client:
        res = client.post('/', data={"text": "Oh great, another Monday"})
        assert res.status_code == 200

