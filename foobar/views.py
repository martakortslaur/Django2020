from django.shortcuts import render


# Create your views here.
def get_first_page(request):
    return render(request, 'foobar/first_page.html')


def get_2020_page(request):
    return render(request, 'foobar/year-2020.html')


def get_ready_page(request):
    return render(request, 'foobar/get_ready.html')


def get_main_page(request):
    return render(request, 'foobar/main_page.html', {'name' : "Marta", 'year' : "2020"})