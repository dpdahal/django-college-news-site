from django.shortcuts import render, HttpResponse
from .models import Blog, Category
from django.db.models import Q


# Create your views here.
def index(request):
    b_data = Blog.objects.filter(is_slider=1)
    latest_news = Blog.objects.all().order_by('-id')
    content = {
        'sliderNews': b_data,
        'latestNews': latest_news,

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
    re = Blog.objects.filter(cat_id=b_g.cat_id)

    # return HttpResponse(re)
    content = {
        'newsData': b_g,
        'relatedNews': re
    }

    return render(request, 'news.html', content)
