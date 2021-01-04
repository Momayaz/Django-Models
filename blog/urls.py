from django.urls import path, include
from .views import HomeView, PostsViews, PostsDetailsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('posts', PostsViews.as_view(), name='all_posts'),
    path('posts/<int:pk>', PostsDetailsView.as_view(), name='post_details'),
]