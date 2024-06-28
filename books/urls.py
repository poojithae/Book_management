# books/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('api/books/', views.book_list, name='book-list'),
    path('api/books/<int:pk>/', views.book_detail, name='book-detail'),
    
]
