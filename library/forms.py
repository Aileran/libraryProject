from django import forms
from .models import Book, Movie, Album
####USER PAGE VVVVV
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#^^^^^^^


#create forms for each collection, this one is for book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'publisher', 'genre', 'comment')


#create form for movie collection
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'director', 'studio', 'genre', 'comment')


#create form for album collection
class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('title', 'artist', 'label', 'genre', 'comment')


        #####################USER PAGE   VVVVVVVVVVVVVV

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
