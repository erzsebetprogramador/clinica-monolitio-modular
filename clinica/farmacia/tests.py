from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Medicamento

User = get_user_model()

class MedicamentoAPITestCase(APITestCase):
    def setUp(self):
        # Crear usuario y token usando el modelo personalizado
        self.user = User.objects.create_user(username="testuser", password="12345")
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

        # Crear medicamento
        Medicamento.objects.create(
            nombre="Ibuprofeno",
            descripcion="Antiinflamatorio",
            stock=30,
            precio=3.0
        )

    def test_listar_medicamentos(self):
        url = reverse('medicamento-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
