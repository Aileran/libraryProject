from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import AlbumForm, BookForm, MovieForm
from .models import Book, Movie, Album
from django.contrib.auth.models import User


# from .forms import UserRegistrationForm
# from django.contrib import messages


# @login_required decorator allows to limit access to the index page and check whether the user is authenticated
# if so, index page is rendered. If not, the user is redirected to the login page via login_url
@login_required(login_url='login')
def index(request):
    # Render the index page
    return render(request, 'library/index.html')


def register_view(request):
    # This function renders the registration form page and create a new user based on the form data
    if request.method == 'POST':
        # We use Django's UserCreationForm which is a model created by Django to create a new user.
        # UserCreationForm has three fields by default: username (from the user model), password1, and password2.
        # If you want to include email as well, switch to our own custom form called UserRegistrationForm
        form = UserCreationForm(request.POST)
        # check whether it's valid: for example it verifies that password1 and password2 match
        if form.is_valid():
            form.save()
            # if you want to login the user directly after saving, use the following two lines instead, and redirect to index
            # user = form.save()
            # login(user)
            # redirect the user to login page so that after registration the user can enter the credentials
            return redirect('login')
    else:
        # Create an empty instance of Django's UserCreationForm to generate the necessary html on the template.
        form = UserCreationForm()
    return render(request, 'library/register.html', {'form': form})


def login_view(request):
    # this function authenticates the user based on username and password
    # AuthenticationForm is a form for logging a user in.
    # if the request method is a post
    if request.method == 'POST':
        # Plug the request.post in AuthenticationForm
        form = AuthenticationForm(data=request.POST)
        # check whether it's valid:
        if form.is_valid():
            # get the user info from the form data and login the user
            user = form.get_user()
            login(request, user)
            # redirect the user to index page
            return redirect('index')
    else:
        # Create an empty instance of Django's AuthenticationForm to generate the necessary html on the template.
        form = AuthenticationForm()
    return render(request, 'library/login.html', {'form': form})


def logout_view(request):
    # This is the method to logout the user
    logout(request)
    # redirect the user to index page
    return redirect('index')


def book(request):
    user = User.objects.get(username=request.user.username)
    user_books = Book.objects.filter(owner=user).order_by('title')
    return render(request, 'library/book_collection.html', {"Books": user_books})


def movie(request):
    user = User.objects.get(username=request.user.username)
    user_movies = Movie.objects.filter(owner=user).order_by('title')
    return render(request, 'library/movie_collection.html', {"Movies": user_movies})


def album(request):
    user = User.objects.get(username=request.user.username)
    user_albums = Album.objects.filter(owner=user).order_by('title')
    return render(request, 'library/album_collection.html', {"Albums": user_albums})


def new_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            media = form.save()
            media.owner = request.user.username
            media.save()
            return redirect('book')
    else:
        form = BookForm()
        context = {'form': form}
        return render(request, 'library/update_book.html', context)


def new_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        # if valid, save form, update new media's "owner" field with username, save to db
        if form.is_valid():
            media = form.save()
            media.owner = request.user.username
            media.save()
            return redirect('movie')
    else:
        form = MovieForm()
        context = {'form': form}
        return render(request, 'library/update_movie.html', context)


def new_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            media = form.save()
            media.owner = request.user.username
            media.save()
            return redirect('album')
    else:
        form = AlbumForm()
        context = {'form': form}
        return render(request, 'library/update_album.html', context)


def delete_book(request, id):
    # Get the product based on its id
    media = Book.objects.get(id=id)
    # if this is a POST request, we need to delete the form data
    if request.method == 'POST':
        media.delete()
        # after deleting redirect to view_product page
        return redirect('book')
    # if the request is not post, render the page with the product's info
    return render(request, 'library/delete_book.html', {'book': media})


def delete_movie(request, id):
    # Get the product based on its id
    media = Movie.objects.get(id=id)
    # if this is a POST request, we need to delete the form data
    if request.method == 'POST':
        media.delete()
        # after deleting redirect to view_product page
        return redirect('movie')
    # if the request is not post, render the page with the product's info
    return render(request, 'library/delete_movie.html', {'movie': media})


def delete_album(request, id):
    # Get the product based on its id
    media = Album.objects.get(id=id)
    # if this is a POST request, we need to delete the form data
    if request.method == 'POST':
        media.delete()
        # after deleting redirect to view_product page
        return redirect('album')
    # if the request is not post, render the page with the product's info
    return render(request, 'library/delete_album.html', {'album': media})


def update_book(request, id):
    # Get the product based on its id
    media = Book.objects.get(id=id)
    # populate a form instance with data from the data on the database
    # instance=product allows to update the record rather than creating a new record when
    # save method is called
    form = BookForm(request.POST or None, instance=media)
    # check whether it's valid:
    if form.is_valid():
        # update the record in the db
        form.save()
        # after updating redirect to view_product page
        return redirect('book')
    # if the request does not have post data, render the page with the form containing the
    # product's info
    return render(request, 'library/update_book.html', {'form': form})


def update_movie(request, id):
    # Get the product based on its id
    media = Movie.objects.get(id=id)
    # populate a form instance with data from the data on the database
    # instance=media allows to update the record rather than creating a new record when
    # save method is called
    form = MovieForm(request.POST or None, instance=media)
    # check whether it's valid:
    if form.is_valid():
        # update the record in the db
        form.save()
        # after updating redirect to view_product page
        return redirect('movie')
    # if the request does not have post data, render the page with the form containing the
    # product's info
    return render(request, 'library/update_movie.html', {'form': form})


def update_album(request, id):
    # Get the product based on its id
    media = Album.objects.get(id=id)
    # populate a form instance with data from the data on the database
    # instance=product allows to update the record rather than creating a new record when
    # save method is called
    form = AlbumForm(request.POST or None, instance=media)
    # check whether it's valid:
    if form.is_valid():
        # update the record in the db
        form.save()
        # after updating redirect to view_product page
        return redirect('album')
    # if the request does not have post data, render the page with the form containing the
    # product's info
    return render(request, 'library/update_album.html', {'form': form})


def add_movie(request):
    if request.method == "POST":
        media = request.POST.get('title')
        Movie.objects.create(title=media, owner=request.user.username)
        return redirect('movie')
    else:
        user = User.objects.get(username=request.user.username)
        user_movies = Movie.objects.filter(owner=user)
        return render(request, 'library/movie_collection.html', {"Movies": user_movies})


def add_book(request):
    if request.method == "POST":
        media = request.POST.get('title')
        Book.objects.create(title=media, owner=request.user.username)
        return redirect('book')
    else:
        user = User.objects.get(username=request.user.username)
        user_books = Book.objects.filter(owner=user)
        return render(request, 'library/book_collection.html', {"Books": user_books})


def add_album(request):
    if request.method == "POST":
        media = request.POST.get('title')
        Album.objects.create(title=media, owner=request.user.username)
        return redirect('album')
    else:
        user = User.objects.get(username=request.user.username)
        user_albums = Album.objects.filter(owner=user)
        return render(request, 'library/album_collection.html', {"Albums": user_albums})


def credits(request):
    return render(request, 'library/credits.html')


def movie_sort(request):
    user = User.objects.get(username=request.user.username)
    user_movies = Movie.objects.filter(owner=user).order_by('title')
    return render(request, 'library/movie_collection.html', {"Movies": user_movies})


def book_sort(request):
    return render(request, 'library/book_collection.html')


def album_sort(request):
    return render(request, 'library/album_collection.html')

