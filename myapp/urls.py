from unicodedata import name
from django.urls import path,re_path,include
from.import views

from django.views.generic import RedirectView


urlpatterns= [
    
    path('',views.results,name='results'),
    path('results',views.results,name='results'),
    path('update',views.update, name='update'),
    #path('user_results',views.user_results, name='user_results'),
    path('update#Search/', RedirectView.as_view(url = '/results#Search/')),
    path('update#Analysis/', RedirectView.as_view(url = '/results#Analysis/')),
    path('index',views.index,name='index'),
    path('login',RedirectView.as_view(url='accounts/login')),
    re_path('accounts/',include('accounts.urls')),
   
    
    #path('api', views.ChartData.as_view()),
]