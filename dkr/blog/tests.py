from django.test import TestCase
from blog.models import Post

class Testing(TestCase):
    def setUp(self):
        self.test_object = Post.objects.create(title='test_title', author='test_author',body='test_body')

    def test_name(self):
        self.assertEqual(self.test_object.title,'test_title')
        self.assertEqual(self.test_object.author, 'test_author')
        self.assertEqual(self.test_object.body, 'test_body')