from app import app

def test_get_students():
    client = app.test_client()
    res = client.get('/students')
    assert res.status_code == 200 
    