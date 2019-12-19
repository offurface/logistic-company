from django.urls import path, include, re_path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.LoginFormView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
]
