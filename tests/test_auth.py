import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_registration(client):
    resp = client.post(reverse('register'), {
        'email': 'test@example.com',
        'password1': 'StrongPass123!',
        'password2': 'StrongPass123!',
    })

    assert resp.status_code == 302
    assert User.objects.filter(email='test@example.com').exists()

@pytest.mark.django_db
def test_login(client):
    User.objects.create_user(email='user@example.com', password='testpass123')

    resp = client.post(reverse('login'), {
        'email': 'user@example.com',
        'password': 'testpass123'
    })

    assert resp.status_code == 302
    assert resp.url == reverse('home')
