from django.urls import path
from apps.base.views import *

urlpatterns = [
    path('', index, name='index_url'),
    path('about_us/', about_us, name='about_url'),
    path('team/', team, name='team_url'),
    path('news/', news, name='news_url'),
    path('post/<int:id>/', news_detail, name='news_detail'),
    path('gallery/', gallery, name='gallery_url'),
    path('contact/', contact, name='contact_url'),
]