from django.urls import path, re_path
from .views import SignupView
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('signup/',SignupView.as_view(),name='signup'),
    re_path(r'^logout/$',auth_views.LoginView.as_view(),name="login"),
]
