from django.urls import path
from . import views
app_name = 'sports'
urlpatterns = [path('', views.sportss, name='home'),
               path('loop/', views.loop, name='house'),
               path('login/', views.jaya, name='login-page'),
               path('logout/', views.out, name='logout-page'),
               path('register/', views.reg, name='register-page'),
               path('blog/', views.blog, name='blog-page'),
               path('team/', views.team, name='team-page'),
               path('contact/', views.contact, name='contact-page'),
               path('news/', views.news, name='news-page'),
               path('about/', views.about, name='about-page'),
               path('search/', views.search, name='searchresult-page'),
               path('readmore/',views.read,name='read-more')]
