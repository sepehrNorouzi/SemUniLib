"""Server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myLibrary import views
import djoser


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.BooksView.as_view(), name="bookList"),
    path('books/recents/', views.RecentBooks.as_view(), name="recentBooks"),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='bookDetail'),
    path('books/favorites/', views.FavoriteView.as_view(), name="Favorites"),
    path('books/toreads/', views.ToReadView.as_view(), name="toReads"),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('books/initialize/', views.initDatabase)
]
