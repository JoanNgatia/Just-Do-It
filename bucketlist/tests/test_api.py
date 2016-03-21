from rest_framework.test import APITestCase, APIClient

url = '/bucketlists/'
url2 = '/bucketlists/<list_id>/'
url3 = '/bucketlists/<list_id>/items/'
url4 = '/bucketlists/<list_id>/items/<item_id>/'
token = '/api-token-auth/'


class BucketlistAppTestCase(APITestCase):
    """Test all bucketlist API endpoints."""

    def setUp(self):
        """Create base details for tests running."""
        self.client = APIClient()
        # Login the user
        auth_user = {'username': 'joan',
                     'password': 'ASHLEY19'}
        login_response = self.client.post(token, auth_user)
        self.token = login_response.data.get('token')

    def test_bucketlist_retrieve(self):
        """Test that bucketlists can be accessed."""
        # unsuccessful access without authentication
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)
