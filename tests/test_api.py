from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    r = client.get('/health')
    assert r.status_code == 200
    assert r.json()['status'] == 'ok'


def test_daily():
    r = client.post('/api/horoscope/daily', json={'sign': 'leo', 'language': 'ro'})
    assert r.status_code == 200
    data = r.json()
    assert data['sign'] == 'leo'
    assert 'summary' in data
