from django.test import SimpleTestCase

class SimpleTests(SimpleTestCase):
    def test_home_page_test(self):
        response=self.client.get('/temp/basic')
        self.assertEqual(response.status_code,200)


    def test_inherit_page_test(self):
        response=self.client.get('/inherit')
        self.assertEqual(response.status_code,200)