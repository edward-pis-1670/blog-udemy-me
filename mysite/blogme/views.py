from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView,CreateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm
from django.urls import reverse_lazy


class AboutView(TemplateView):
    template_name = 'blogme/post_list.html'

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blogme/post_detail.html'

    form_class = PostForm

    model = Post




