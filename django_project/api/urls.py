from django.urls import path, include
from .views import main, UserView, CreateUserView, FindUserView, DeleteUserView

urlpatterns = [
    path('', main),
    path('user', UserView.as_view()),
    path('user/<int:id>', FindUserView.as_view()),
    path('user/<int:id>', DeleteUserView.as_view()),
    path('create-user', CreateUserView.as_view())
]