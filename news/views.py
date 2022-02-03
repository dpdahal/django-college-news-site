from django.shortcuts import render, HttpResponse
from .models import Blog


# Create your views here.
def index(request):
    b_data = Blog.objects.filter(is_slider=1)
    latest_news = Blog.objects.all().order_by('-id')
    content = {
        'sliderNews': b_data,
        'latestNews': latest_news
    }
    return render(request, 'index.html', content)


def about(request):
    return render(request, 'about.html')


def contact(request):
    content = {
        'title': "Contact-us",

    }
    return render(request, 'contact.html', content)


def news_details(request, slug):
    b_g = Blog.objects.filter(slug=slug).get()
    b_g.page_visit += 1
    b_g.save()
    content = {
        'newsData': b_g
    }

    return render(request, 'news.html', content)
