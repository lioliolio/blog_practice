from django.views.generic import View

from blog.models import Post


class PostBaseView(View):
    model = Post
