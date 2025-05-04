from django.urls import path
from .views import UserCreateView, BlogPostCreateView, BlogPostListView, UserLoginView

urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),  # This is the login endpoint
    path('posts/create/', BlogPostCreateView.as_view(), name='post-create'),
    path('posts/', BlogPostListView.as_view(), name='post-list'),
]