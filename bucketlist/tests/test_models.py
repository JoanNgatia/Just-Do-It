from django.test import TestCase
from bucketlist.models import Account, Bucketlist, Bucketlistitem


class BucketModelsTest(TestCase):
    """Test accurate creation of models."""

    # Include 1 user,3 bucketlists and 4 bucketlistitems for testing purposes
    fixtures = ['bucketlist.json']

    def setUp(self):
        """Set up new dummy data."""
        self.account = Account.objects.create(
            username='test',
            password='test')
        self.bucketlist = Bucketlist.objects.create(
            name='test_bucketlist', creator=self.account)
        self.bucketitem = Bucketlistitem.objects.create(
            name='test_bucketitem', bucketlist=self.bucketlist)

    def tearDown(self):
        """Clean up database after successful test run."""
        Account.objects.all().delete()
        Bucketlist.objects.all().delete()
        Bucketlistitem.objects.all().delete()

    def test_account_creation(self):
        """Test that accounts/users are created."""
        self.assertEqual(self.account.get_username(), 'test')
        self.assertIsInstance(self.account, Account)

    def test_bucketlist_creation(self):
        """Test that bucketlists are created."""
        self.assertTrue(Bucketlist.objects.all())
        self.assertIn('test_bucketlist',
                      Bucketlist.objects.get(name='test_bucketlist').name)
        self.assertEqual(Bucketlist.objects.count(), 4)
        self.assertIsInstance(self.bucketlist, Bucketlist)

    def test_bucketlistitem_creation(self):
        """Test that items are created."""
        self.assertTrue(Bucketlistitem.objects.all())
        self.assertIn('test_bucketitem', Bucketlistitem.objects.get(
            name='test_bucketitem').name)
        self.assertEqual(Bucketlistitem.objects.count(), 5)
        self.assertIsInstance(self.bucketitem, Bucketlistitem)
