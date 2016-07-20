from django.test import TestCase, LiveServerTestCase, Client
from django.utils import timezone
from blog.models import Post

# Create your tests here.
class PostTest(TestCase):
    def test_create_post(self):
        post = Post()

        post.title = 'My first post'
        post.text = 'This is my first blog post'
        post.pub_date = timezone.now()

        post.save()

        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts), 1)
        only_post  = all_posts[0]
        self.assertEquals(only_post, post)

         # Check attributes
        self.assertEquals(only_post.title, 'My first post')
        self.assertEquals(only_post.text, 'This is my first blog post')
        self.assertEquals(only_post.pub_date.day, post.pub_date.day)
        self.assertEquals(only_post.pub_date.month, post.pub_date.month)
        self.assertEquals(only_post.pub_date.year, post.pub_date.year)
        self.assertEquals(only_post.pub_date.hour, post.pub_date.hour)
        self.assertEquals(only_post.pub_date.minute, post.pub_date.minute)
        self.assertEquals(only_post.pub_date.second, post.pub_date.second)


class AdminTest(LiveServerTestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.client = Client()

    def test_login(self):

        # Get login page
        response = self.client.get('/admin/', follow=True)

        # Check response code
        self.assertEquals(response.status_code, 200)

        # Check 'Log in' in response
        self.assertTrue('Log in' in response.content.decode('utf-8'))

        # Log the user in
        self.client.login(username='bobsmith', password="password")

        # Check response code
        response = self.client.get('/admin/')
        self.assertEquals(response.status_code, 200)

        # Check 'Log out' in response
        self.assertTrue('Log out' in response.content.decode('utf-8'))

    def test_logout(self):

        # Log in
        self.client.login(username='bobsmith', password="password")

        # Check response code
        response = self.client.get('/admin/')
        self.assertEquals(response.status_code, 200)

        # Check 'Log out' in response
        self.assertTrue('Log out' in response.content.decode('utf-8'))

        # Log out
        self.client.logout()

        # Check response code
        response = self.client.get('/admin/', follow=True)
        self.assertEquals(response.status_code, 200)

        # Check 'Log in' in response
        self.assertTrue('Log in' in response.content.decode('utf-8'))


    def test_create_post(self):

        # Log in
        self.client.login(username='bobsmith', password="password")

        # Check response code
        response = self.client.get('/admin/blog/post/add/')
        self.assertEquals(response.status_code, 200)

        # Create the new post
        response = self.client.post('/admin/blog/post/add/', {
            'title': 'My first post',
            'text': 'This is my first post',
            'pub_date_0': '2013-12-28',
            'pub_date_1': '22:00:04'
        },
        follow=True
        )
        self.assertEquals(response.status_code, 200)

        # Check added successfully
        self.assertTrue('added successfully' in response.content.decode('utf-8'))

        # Check new post now in database
        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts), 1)

    def test_edit_post(self):

        # Create the post
        post = Post()
        post.title = 'My first post'
        post.text = 'This is my first blog post'
        post.pub_date = timezone.now()
        post.save()
        print(post.title)
        print(post.__dict__)
        id = post.id

        # Log in
        self.client.login(username='bobsmith', password="password")

        # Edit the post
        response = self.client.post('/admin/blog/post/%d/' % id, {
            'title': 'My second post',
            'text': 'This is my second blog post',
            'pub_date_0': '2013-12-28',
            'pub_date_1': '22:00:04'
        },
        follow=True
        )
        self.assertEquals(response.status_code, 200)

        # Check changed successfully
        self.assertTrue('changed successfully' in response.content.decode('utf-8'))

        # Check post amended
        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts), 1)
        only_post = all_posts[0]
        self.assertEquals(only_post.title, 'My second post')
        self.assertEquals(only_post.text, 'This is my second blog post')

    def test_delete_post(self):
        # Create the post
        post = Post()
        post.title = 'My second post'
        post.text = 'This is second blog post'
        post.pub_date = timezone.now()
        post.save()
        id = post.id

        # Check new post saved
        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts), 1)

        # Log in
        self.client.login(username='bobsmith', password="password")

        # Delete the post
        response = self.client.post('/admin/blog/post/%d/delete/' % id, {
            'post': 'yes'
        }, follow=True)
        self.assertEquals(response.status_code, 200)

        # Check deleted successfully
        self.assertTrue('deleted successfully' in response.content.decode('utf-8'))

        # Check post amended
        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts), 0)
