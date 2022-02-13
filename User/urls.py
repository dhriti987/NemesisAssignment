from django.urls import path

from User.views import UserUpdateDeleteView, UserView, home,sign_up,login

urlpatterns = [
    path('',login),
    path('user/',UserView.as_view()),
    path('user/<int:pk>',UserUpdateDeleteView.as_view()),
    path('home/',home),
    path('signup/',sign_up),
]
