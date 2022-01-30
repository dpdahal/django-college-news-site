from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    content = {
        'title': "Contact-us"
    }
    return render(request, 'contact.html', content)
