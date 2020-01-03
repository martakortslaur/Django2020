from django.shortcuts import render

# Create your views here.
def get_second_page(request):
    return render(request, 'testing/second_page.html')