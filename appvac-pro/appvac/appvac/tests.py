from django.test import TestCase
from .models import Proyecto

# Create your tests here.

class ProyectoModelTest(TestCase):
    def test_creacion_proyecto(self):
        proyecto = Proyecto.objects.create(
            titulo='Proyecto de Prueba',
            descripcion='Descripción de prueba.',
            fecha='2024-01-01',
            enlace='http://example.com'
        )
        self.assertEqual(proyecto.titulo, 'Proyecto de Prueba')
