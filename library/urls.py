from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import (
    BookListView,
    BookDetailView,
    BookUpdateView,
    BookDeleteView,
    BookCreateView
    )



urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('rules/', views.rules, name='rules'),
    path('book_update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('book_delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),
    path('book_create/', BookCreateView.as_view(), name='book_create'),    
]