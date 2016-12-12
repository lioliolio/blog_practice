from django.shortcuts import render

from blog.models import NaverPost


def naver_posts_list(request):
    return render(
        request,
        "naver_posts/list.html",
        {
            "naver_posts": NaverPost.objects.all(),
        },
    )
