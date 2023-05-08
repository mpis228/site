from django.urls import path, include
from .views import *


from django.views.generic import TemplateView

urlpatterns = [
    path('', Home.as_view(), name='main'),
    path('forum/', Forum.as_view(), name="forum"),
    path('home/', Home.as_view(), name="home"),
    path('register/', Register.as_view(), name='reg'),
    path("shop/", Shop.as_view(), name="shop"),
    path('feedback/', FeedBack.as_view(), name='feedback'),
    path("user/", include("django.contrib.auth.urls")),
]