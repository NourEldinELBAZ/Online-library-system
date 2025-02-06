from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('home/', views.homepage, name='home'),
    path('viewbooks/', include('libraryapp.urls')),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('addbook/', views.add_book, name='add_book'),
    path('borrowedbooks/', views.borrowed_books, name='borrowed_books'),
    path('search/', views.search_books, name='search_books'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
