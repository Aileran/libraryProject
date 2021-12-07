from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('book/', views.book, name='book'),
    path('movie/', views.movie, name='movie'),
    path('album/', views.album, name='album'),
    path('book/new_book/', views.new_book, name='new_book'),
    path('movie/new_movie/', views.new_movie, name='new_movie'),
    path('album/new_album/', views.new_album, name='new_album'),
    path('book/update_book/<int:id>', views.update_book, name='update_book'),
    path('movie/update_movie/<int:id>', views.update_movie, name='update_movie'),
    path('album/update_album/<int:id>', views.update_album, name='update_album'),
    path('book/delete_book/<int:id>', views.delete_book, name='delete_book'),
    path('movie/delete_movie/<int:id>', views.delete_movie, name='delete_movie'),
    path('album/delete_album/<int:id>', views.delete_album, name='delete_album'),
    path('movie/add_movie/', views.add_movie, name='add_movie'),
    path('book/add_book/', views.add_book, name='add_book'),
    path('album/add_album/', views.add_album, name='add_album'),
    path('credits/', views.credits, name='credits'),
]
