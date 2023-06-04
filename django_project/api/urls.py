from django.urls import path, include
from .views import main, UserListView, CreateUserView, UserDetailsView, LoginView, RefreshTokenView

urlpatterns = [
    path('', main),
    path('user', UserListView.as_view()),
    path('refresh-token', RefreshTokenView.as_view()),
    path('user/<int:id>', UserDetailsView.as_view()),
    path('login', LoginView.as_view()),    
    path('create-user', CreateUserView.as_view())
]