from django.urls import path, include
from .views import main, UserListView, CreateUserView, UserDetailsView

urlpatterns = [
    path('', main),
    path('user', UserListView.as_view()),
    path('user/<int:id>', UserDetailsView.as_view()),    
    path('create-user', CreateUserView.as_view())
]