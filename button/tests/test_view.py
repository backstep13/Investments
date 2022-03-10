from django.test import TestCase


class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """Test of load properly template of start page"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_register_loads_properly(self):
        """Test of working register page"""
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_not_auth_profile_loads_properly(self):
        """Test redirect function if user is not authenticated"""
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
