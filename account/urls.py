from django.urls import path
from .views import SignUp,change_password

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('password/', change_password, name='change_password'),
]