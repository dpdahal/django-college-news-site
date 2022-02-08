from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('category/<id>', views.cat_news_list, name='category'),
    path('news-details/<slug>', views.news_details, name='news-details')
]
