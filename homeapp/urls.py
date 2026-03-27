from django.urls import path 
from .views import Homeview , Aboutview , Userview

urlpatterns=[
    path('', Homeview.as_view(),name='home'),
    path('about/', Aboutview.as_view(),name='about'),
    path('login/',Userview.as_view(), name='login')
]