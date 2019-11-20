from django.urls import path
from . import views
from .views import UserLoginView,UserLogoutView,UserRegisterFormView




app_name="users"
urlpatterns = [
    path('login/',UserLoginView.as_view(),name="login"),
    path('logout/',UserLogoutView.as_view(),name="logout"),
    path('register/', UserRegisterFormView.as_view(), name='register'),
]