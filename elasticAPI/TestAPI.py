import requests

def test_serverup():
	r = requests.get('http://localhost:8000')

	assert r.status_code == 200