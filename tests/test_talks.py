from unittest import TestCase
from talkshow.app import create_app

class TestRoute(TestCase):
    
    def setUp(self):
        self.client = create_app().test_client()

    def test_status_index_route(self):
        response = self.client.get('/talks/')
        self.assertEqual(200, response.status_code)
    
    




