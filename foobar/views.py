from django.shortcuts import render
from .models import Movies
from .forms import MoviesForm

# Create your views here.
def get_first_page(request):
    return render(request, 'foobar/first_page.html')


def get_2020_page(request):
    return render(request, 'foobar/year-2020.html')


def get_ready_page(request):
    return render(request, 'foobar/get_ready.html')


def get_main_page(request):
    names = ["Darragh", "Marta", "Rory", "Xav"]
    return render(request, 'foobar/main_page.html',
                {'names' : names, 'year' : "2020"})


def get_movies(request):
    movies = Movies.objects.all()
    return render(request, 'foobar/movies.html', {"movies": movies})


def create_movie(request):

    if request.method == "GET":
        return render(request, 'foobar/create_movie.html')
    
    if request.method == "POST":
        form = MoviesForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()

            return render(request, "foobar/movie-creation-confirmed.html")