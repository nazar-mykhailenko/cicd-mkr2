from django.shortcuts import render
from django.db.models import Count
from .models import Author, Book

# Create your views here.
def main(request):
    books = Book.objects.filter()[:5]
    return render(request, 'book_list.html', {
        'books': books,
    })

def book_list(request):
    authors = Author.objects.annotate(book_count=Count('book'))
    return render(request, 'author_list.html', {
        'authors': authors
    })
