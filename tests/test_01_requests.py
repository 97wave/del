import pytest
from django.test import Client, client

class Test01Requests:
    client = Client

    @pytest.mark.django_db(transaction=True)
    def test_01_user_created(self):
        response = client.get('/projects/')
        assert response.status_code in [200, 201], f"request failed with code {response.status_code}"

    @pytest.mark.django_db(transaction=True)
    def test_01_user_created(self):
        response = client.post('/projects/')
        assert response.status_code in [200, 201], f"request failed with code {response.status_code}"
        
    @pytest.mark.django_db(transaction=True)
    def test_01_user_created(self):
        response = client.put('/projects/5')
        assert response.status_code in [200, 201], f"request failed with code {response.status_code}"
        
    @pytest.mark.django_db(transaction=True)
    def test_01_user_created(self):
        response = client.patch('/projects/2')
        assert response.status_code in [200, 201], f"request failed with code {response.status_code}"
        
    @pytest.mark.django_db(transaction=True)
    def test_01_user_created(self):
        response = client.delete('/projects/3')
        assert response.status_code in [200, 201, 204], f"request failed with code {response.status_code}"
    