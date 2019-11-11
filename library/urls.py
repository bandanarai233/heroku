from django.urls import path
from . import views
from .views import (
    BookListView,
    BookDetailView,
    BookUpdateView,
)



urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book_update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),

]