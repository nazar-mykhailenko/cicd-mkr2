from django.test import TestCase, Client
from .models import Author, Book

class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.author = Author.objects.create(name='Test Author')
        self.book = Book.objects.create(title='Test Book', description='Test Description', price=10.99, publication_date='2022-04-20')
        self.book.authors.add(self.author)

    def test_main_view(self):
        response = self.client.get('/main')
        self.assertEqual(response.status_code, 200)

    def test_author_list_view(self):
        response = self.client.get('/author-list')
        self.assertEqual(response.status_code, 200)