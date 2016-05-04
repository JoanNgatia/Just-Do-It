from rest_framework.test import APITestCase
from django.core.urlresolvers import reverse

from bucketlist.models import Account, Bucketlist, Bucketlistitem

message = {"detail":
           "Authentication credentials were not provided."}
auth = '/api/token/'
url_register_new_user = '/api/v1/users/'
url_for_all_bucketlists = '/api/v1/bucketlists/'
url_for_one_bucketlist = '/api/v1/bucketlists/2/'
url_for_unauthorized_bucketlist = '/api/v1/bucketlists/4/'
url_to_create_new_item = '/api/v1/bucketlists/2/items/'
url_for_one_bucketlist_item = '/api/v1/bucketlists/2/items/2/'
url_for_nonexistent_bucketlist = '/api/v1/bucketlists/8/'
not_found_msg = {"detail": "Not found."}


class BucketListApiTest(APITestCase):
    """Test all bucketlist resource endpoints."""

    # Include 1 user,3 bucketlists and 4 bucketlistitems for testing purposes
    fixtures = ['bucketlist.json']

    def setUp(self):
        """Create base authentication details."""
        token_url = reverse('token')
        data = {
            'username': 'joan', 'password': 'ASHLEY19'}
        self.response = self.client.post(token_url, data)
        self.token = self.response.data.get('token')

    def test_user_creation(self):
        """Test that a new user can be registered in the system."""
        response = self.client.post(
            url_register_new_user, {'username': 'ashley',
                                    'password': 'ashley',
                                    'tagline': 'ashley'})
        self.assertEqual(response.status_code, 201)

    def test_bucketlist_retrieval(self):
        """Test that bucketlists can be retrieved from the DB."""
        response = self.client.get(url_for_all_bucketlists)
        self.assertEqual(response.status_code, 401)

        auth_response = self.client.get(url_for_unauthorized_bucketlist)
        self.assertEqual(auth_response.status_code, 401)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        auth_response = self.client.get(url_for_all_bucketlists)
        self.assertEqual(auth_response.status_code, 200)
        self.assertEqual(auth_response.data['count'], 3)

        auth_response = self.client.get(url_for_one_bucketlist)
        self.assertEqual(auth_response.status_code, 200)
        self.assertEqual(auth_response.data.get('name'), 'Temperature')

    def test_bucketlist_creation(self):
        """Test that bucketlists can be added to the DB."""
        new_bl = {'name': 'Go to Rio'}

        response = self.client.post(url_for_all_bucketlists, new_bl)
        self.assertEqual(response.status_code, 401)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        auth_response = self.client.post(url_for_all_bucketlists, new_bl)
        self.assertEqual(auth_response.status_code, 201)
        self.assertEqual(auth_response.data.get('name'), 'Go to Rio')
        self.assertEqual(Bucketlist.objects.count(), 5)

    def test_bucketlist_edition(self):
        """Test that existing bucketlists can be edited."""
        edited_bl = {'name': 'Catch mafeelings'}

        response = self.client.put(url_for_one_bucketlist, edited_bl)
        self.assertEqual(response.data, message)
        self.assertEqual(response.status_code, 401)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        auth_response = self.client.put(url_for_one_bucketlist, edited_bl)
        self.assertEqual(auth_response.status_code, 200)
        self.assertEqual(auth_response.data.get('name'), 'Catch mafeelings')

        auth_response = self.client.put(
            url_for_nonexistent_bucketlist, edited_bl)
        self.assertEqual(auth_response.status_code, 404)
        self.assertEqual(auth_response.data, not_found_msg)

    def test_bucketlist_deletion(self):
        """Test that existing bucketlists can be deleted from the DB."""
        response = self.client.delete(url_for_one_bucketlist)
        self.assertEqual(response.data, message)
        self.assertEqual(response.status_code, 401)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        auth_response = self.client.delete(url_for_one_bucketlist)
        self.assertEqual(auth_response.status_code, 204)
        self.assertEqual(Bucketlist.objects.count(), 3)

    def test_bucketlistitem_creation(self):
        """Test that a bucketlistitem can be added to a bucketlist."""
        new_item = {'name': 'Zigo Remix', 'bucketlist': 2}

        response = self.client.post(url_to_create_new_item, new_item)
        self.assertEqual(response.data, message)
        self.assertEqual(response.status_code, 401)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        auth_response = self.client.post(url_to_create_new_item, new_item)
        self.assertEqual(auth_response.status_code, 201)
        self.assertEqual(auth_response.data.get('name'), 'Zigo Remix')
        self.assertEqual(Bucketlistitem.objects.count(), 5)
        self.assertEqual(
            Bucketlistitem.objects.filter(name='Zigo Remix').
            first().bucketlist_id, 2)

    def test_bucketlistitem_edition(self):
        """Test that a bucketlistitem can be updated."""
        edited_item = {'name': 'Unconditionally Bae', 'bucketlist': 2}

        response = self.client.put(url_for_one_bucketlist_item, edited_item)
        self.assertEqual(response.data, message)
        self.assertEqual(response.status_code, 401)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        auth_response = self.client.put(
            url_for_one_bucketlist_item, edited_item)
        self.assertEqual(auth_response.status_code, 200)
        self.assertEqual(auth_response.data.get('name'), 'Unconditionally Bae')

    def test_bucketlistitem_deletion(self):
        """Test that a bucketlist item can be deleted."""
        response = self.client.delete(url_for_one_bucketlist_item)
        self.assertEqual(response.data, message)
        self.assertEqual(response.status_code, 401)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        auth_response = self.client.delete(url_for_one_bucketlist_item)
        self.assertEqual(auth_response.status_code, 204)
        self.assertEqual(Bucketlistitem.objects.count(), 3)
