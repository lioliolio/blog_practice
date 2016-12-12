from django.shortcuts import render

from blog.models import NaverPost


def naver_posts_list(request):
    keyword = request.GET.get("keyword")
    query = request.GET.get("query")
    naver_posts = NaverPost.objects.all()

    if keyword:
        naver_posts = naver_posts.filter(keyword=keyword)

    if query:
        naver_posts = naver_posts.filter(title__contains=query)

    return render(
        request,
        "naver_posts/list.html",
        {
            "query": query,
            "keyword": keyword,
            "naver_posts": naver_posts,
        },
    )
