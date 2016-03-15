import requests

def test_serverup():
	r = requests.get('http://localhost:8000')

	assert r.status_code == 200
	


def test_api_get():
	r = requests.get('http://localhost:8000/v1/homedepot/deals?status=active')

	assert r.status_code == 200



def test_api_post():
	r = requests.post('http://localhost:8000/v1/homedepot/deals?status=active')

	assert r.status_code == 403



def test_api_put():
	r = requests.put('http://localhost:8000/v1/homedepot/deals?status=active')

	assert r.status_code == 403



def test_api_delete():
	r = requests.delete('http://localhost:8000/v1/homedepot/deals?status=active')

	assert r.status_code == 403