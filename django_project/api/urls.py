from django.urls import path, include
from .views import UserView

urlpatterns = [
    path('user', UserView.as_view())
]