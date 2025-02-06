from django.urls import path
from . import views

urlpatterns = [
    path('' , views.viewbooks, name='viewbooks'),
    path('bookdetails/<int:book_id>/', views.viewbookdetails, name='bookdetails'),
    path('editbook/<int:book_id>/',views.editbook, name='editbook'),
    path('deletebook/<int:book_id>/', views.delete_book, name='delete_book'),
    path('borrowbook/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('returnbook/<int:book_id>/', views.return_book, name='return_book'),
]
