from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post
# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

class PostsViews(ListView):
    template_name = 'all_posts.html'
    model = Post

class PostsDetailsView(DetailView):
    template_name = 'post_details.html'
    model = Post