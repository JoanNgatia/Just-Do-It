from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from bucketlist.models import Account, Bucketlist, Bucketlistitem


class TestBucketlistView(TestCase):
    """Test django bucketlist views."""

    # Include 1 user,4 bucketlists and 4 bucketlistitems as dummy data
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
        self.bucketlistitem = Bucketlistitem.objects.create(
            name='test_bucketlistitem', bucketlist=self.bucketlist)

    def tearDown(self):
        """Databse clean up after successful test run."""
        Account.objects.all().delete()
        Bucketlist.objects.all().delete()

    def test_user_registration(self):
        """Test that a new user can get registered on the system."""
        response = self.client.post(reverse('register'),
                                    {'username': 'test',
                                     'password': 'test',
                                     'confirm_password': 'test'})
        self.assertEqual(response.status_code, 302)

    def test_user_login(self):
        """Test that a registered user can login."""
        response = self.client.post(reverse('login'),
                                    {'username': 'test',
                                     'password': 'test'})
        self.assertEqual(response.status_code, 302)

        # Test that a non-registered user cannot login
        response = self.client.post(reverse('login'),
                                    {'username': 'not test',
                                     'password': 'test'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/login')

    def test_user_logout(self):
        """Test that a logged in user can logout."""
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_can_access_bucketlists_view(self):
        """Test that a logged in user can access their bucketlists."""
        response = self.client.get(
            reverse('all_bucketlists'))
        self.assertEqual(response.status_code, 200)

    def test_access_to_bucketlist_creation(self):
        """Test that a user can create a bucketlist."""
        # successful creation
        response = self.client.post(
            reverse('all_bucketlists'), {'name': 'Lets go to the zoo'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Bucketlist.objects.count(), 5)

        # unsuccessful creation
        response = self.client.post(
            reverse('all_bucketlists'), {'name': ''})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/bucketlist')

    def test_access_to_bucketlist_update(self):
        """Test that a user can edit a bucketlist."""
        response = self.client.post(
            reverse('single_bucketlist_edit',
                    kwargs={'pk': self.bucketlist.id}),
            {'name': 'Lets go to the zoo'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Bucketlist.objects.count(), 4)

    def test_access_to_bucketlist_deletion(self):
        """Test that a user can deletet a bucketlist."""
        response = self.client.get(
            reverse('single_bucketlist_delete',
                    kwargs={'pk': self.bucketlist.id}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Bucketlist.objects.count(), 3)

    def test_access_to_bucketlistitems(self):
        """Test that a user can view items in their bucketlists."""
        response = self.client.get(
            reverse('bucketlistitems_get',
                    kwargs={'pk': self.bucketlist.id}))
        self.assertEqual(response.status_code, 200)

    def test_addition_of_bucketlist_items(self):
        """Test that a user can create a bucketlist item."""
        response = self.client.post(
            reverse('bucketlistitems_get', kwargs={'pk': self.bucketlist.id}),
            {'name': 'MAdtraxx!!'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Bucketlistitem.objects.count(), 6)

        # unsuccessful item creation
        response = self.client.post(
            reverse('bucketlistitems_get', kwargs={'pk': self.bucketlist.id}),
            {'name': ''})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Bucketlistitem.objects.count(), 6)

    def test_edition_of_bucketlistitems(self):
        """Test that a user can change the name of a bucketlist item."""
        response = self.client.post(
            reverse('bucketlistitems_update',
                    kwargs={'pk': self.bucketlistitem.id,
                            'bucketlist': self.bucketlist.id}),
            {'name': 'MAdtraxx!!'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Bucketlistitem.objects.count(), 5)
        self.assertEqual(
            Bucketlistitem.objects.get(id=self.bucketlistitem.id).name,
            'MAdtraxx!!')

    def test_deletion_of_bucketlistitem(self):
        """Test that a user can delete a bucektlist item."""
        response = self.client.get(
            reverse('bucketlistitems_delete',
                    kwargs={'pk': self.bucketlistitem.id,
                            'bucketlist': self.bucketlist.id}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Bucketlistitem.objects.count(), 4)

    def test_edition_of_bucektlistitem_status(self):
        """Test that a user can change the status of a bucketlist item."""
        response = self.client.get(
            reverse('bucketlistitems_status',
                    kwargs={'pk': self.bucketlistitem.id,
                            'bucketlist': self.bucketlist.id}))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Bucketlistitem.objects.get(id=self.bucketlistitem.id).done)
