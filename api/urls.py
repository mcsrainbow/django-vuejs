from django.urls import path
from .views import add_book, show_books, delete_book

urlpatterns = [
    path('add_book/', add_book, name='add_book'),
    path('show_books/', show_books, name='show_books'),
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),
]