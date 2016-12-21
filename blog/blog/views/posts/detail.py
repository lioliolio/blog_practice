from django.views.generic.detail import DetailView

from blog.models import Post

from .base import PostBaseView


class PostDetailView(PostBaseView, DetailView):
    template_name = "posts/detail.html"
