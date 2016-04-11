from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from bucketlist.models import Account, Bucketlist, Bucketlistitem


class TestBucketlistView(TestCase):
    """Test django bucketlist views."""

    # Include 1 user,3 bucketlists and 4 bucketlistitems as dummy data
    fixtures = ['bucketlist.json']

    def setUp(self):
        """Create base data for testing."""
        self.client = Client()
        self.user = Account.objects.create_user(
            username='test',
            password='test'
        )
        self.user.set_password('test')
        self.user.save()
        self.login = self.client.login(
            username='test', password='test')
        self.bucketlist = Bucketlist.objects.create(
            name='test_bucketlist', creator=self.user)

    def tearDown(self):
        """Databse clean up aftr successful test run."""
        Account.objects.all().delete()
        Bucketlist.objects.all().delete()

    def test_can_access_bucketlists_view(self):
        """Test that a logged in user can access their bucketlists."""
        response = self.client.get(
            reverse('all_bucketlists'))
        self.assertEqual(response.status_code, 200)
