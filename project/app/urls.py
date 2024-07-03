
from django.urls import path,include

from .views import register
from .views import registerdata

from app import views
urlpatterns = [
    # path('home/',home)        it show directly import
    path('register/', views.register ),
    path('registerdata/', views.registerdata,name='register')
]
