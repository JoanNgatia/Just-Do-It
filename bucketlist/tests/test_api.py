from rest_framework.test import APITestCase
from django.core.urlresolvers import reverse

from bucketlist.models import Account, Bucketlist, Bucketlistitem

message = {"detail":
           "Authentication credentials were not provided."}
auth = '/api/token/'
url = '/api/v1/bucketlists/'
url2 = '/api/v1/bucketlists/1/'
url3 = '/api/v1/bucketlists/1/items/'
url4 = '/api/v1/bucketlists/1/items/1/'
not_found_msg = {"detail": "Not found."}


class BucketListApiTest(APITestCase):
    """Test all bucketlist resource endpoints."""

    def setUp(self):
        """Create base authentication details."""
        self.username = 'mama'
        self.passsword = 'ashley'
        self.user = Account.objects.create_user(
            username=self.username, password=self.passsword)
        url = reverse('token')
        data = {'username': self.username, 'password': self.passsword}
        self.response = self.client.post(url, data)
        self.token = self.response.data.get('token')

    def test_bucketlist_retrieval(self):
        """Test that bucketlists can be retrieved from the DB."""
        # unsuccessful retrieval w/out authentication
        response = self.client.get(url)
        self.assertEqual(response.data, message)
        self.assertEqual(response.status_code, 401)

        # add authentication to client
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        # successful retrieval
        auth_response = self.client.get(url)
        self.assertEqual(auth_response.status_code, 200)

    def test_bucketlist_creation(self):
        """Test that bucketlists can be added to the DB."""
        new_bl = {'name': 'Go to Rio'}
        # unsuccessful retrieval w/out authentication
        response = self.client.post(url, new_bl)
        self.assertEqual(response.data, message)
        self.assertEqual(response.status_code, 401)

    def test_bucketlist_edition(self):
        """Test that existing bucketlists can be edited."""
        edited_bl = {'name': 'Go to Rio'}
        # unsuccessful retrieval w/out authentication
        response = self.client.put(url, edited_bl)
        self.assertEqual(response.data, message)
        self.assertEqual(response.status_code, 401)

    def test_bucketlist_deletion(self):
        """Test that existing bucketlists can be deleted from the DB."""
        # unsuccessful removal w/out authentication
        response = self.client.delete(url2)
        self.assertEqual(response.data, message)
        self.assertEqual(response.status_code, 401)
