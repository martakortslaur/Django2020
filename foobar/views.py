from django.shortcuts import render, get_object_or_404, redirect
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
        form = MoviesForm()
        return render(request, 'foobar/create_movie.html', {'form': form})
    
    if request.method == "POST":
        form = MoviesForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()

            return render(request, "foobar/movie-creation-confirmed.html")

def update_movie(request, pk):

    if request.method == "GET":
        movie = get_object_or_404(Movies, pk=pk)
        form = MoviesForm(instance=movie)
        return render(request, "foobar/movie-update.html", {'form': form, 'id': pk})

    if request.method == 'POST':
        movie = get_object_or_404(Movies, pk=pk)
        form = MoviesForm(request.POST, instance=movie)
        form.save()
        return render(request, "foobar/movie-creation-confirmed.html")

def delete_movie(request, pk):
    movie = get_object_or_404(Movies, pk=pk)
    movie.delete()
    return redirect('get_movies')
