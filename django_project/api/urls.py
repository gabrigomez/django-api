from django.urls import path, include
from .views import main, UserView, CreateUserView

urlpatterns = [
    path('', main),
    path('user', UserView.as_view()),
    path('create-user', CreateUserView.as_view())
]