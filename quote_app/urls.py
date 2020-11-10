from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('success', views.success),
    path('add_quote', views.add_quote),
    path('myaccount/<int:id>', views.account_page),
    path('update/<int:id>', views.update),
    path('user/<int:id>', views.user_page),
    path('like', views.like),
    path('delete/<int:id>', views.delete)
]