import unittest
from main import app, obtener_coordenadas, obtener_temperatura

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        # Configura la aplicación Flask para pruebas
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        # Envía una solicitud GET al índice y verifica la respuesta
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Bogotá', response.data.decode('utf-8'))
        self.assertIn('Miami', response.data.decode('utf-8'))
        self.assertIn('Londres', response.data.decode('utf-8'))
        self.assertIn('Tokio', response.data.decode('utf-8'))

    def test_comparacion(self):
        # Simula un POST al endpoint /comparacion
        response = self.app.post('/comparacion', data={
            'ciudad_1': 'Bogotá',
            'ciudad_2': 'Miami',
            'ciudad_3': 'Londres'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Bogotá', response.data.decode('utf-8'))
        self.assertIn('Miami', response.data.decode('utf-8'))
        self.assertIn('Londres', response.data.decode('utf-8'))

    def test_obtener_coordenadas(self):
        self.assertEqual(obtener_coordenadas('Bogotá'), (4.71, -74.07))
        self.assertEqual(obtener_coordenadas('Miami'), (25.76, -80.19))
        self.assertEqual(obtener_coordenadas('Londres'), (51.51, -0.13))
        self.assertEqual(obtener_coordenadas('Tokio'), (35.68, 139.76))

    def test_obtener_temperatura(self):
        # Aquí debes hacer un mock de la función requests.get para devolver un valor controlado
        import requests
        from unittest.mock import patch

        class MockResponse:
            @staticmethod
            def json():
                return {
                    "current": {
                        "temp": 20.0
                    }
                }

        with patch.object(requests, 'get', return_value=MockResponse()):
            self.assertEqual(obtener_temperatura(4.71, -74.07), 20.0)

if __name__ == '__main__':
    unittest.main()