import json
import requests

from django.http.response import HttpResponse
from django.conf import settings


def home(request):
    return HttpResponse("<h1>Hello World!</h1><p>This is my blog!!!</p>")

def room(request, room_id):
    url = "https://api.zigbang.com/v1/items?detail=true&item_ids=" + room_id
    response = requests.get(url)
    return HttpResponse(
            response.content,
            content_type="application/json",
    )

def news(request):

    search = request.GET.get("search")

    url = "https://watcha.net/home/news.json?page=1&per=50"
    response = requests.get(url)

    news_dict = json.loads(response.text)
    news_list = news_dict.get("news")

    if search:
        news_list = list(filter(
            lambda news: search in news.get("title"),
            news_list,
        ))

    with open(settings.BASE_DIR + "/blog/templates/news.html", "r") as template:
        content = template.read()

        content += "{count} 개의 뉴스 정보가 있습니다.".format(count=len(news_list)) +\
            "".join([
                "<h2>{title}</h2><img src={image_src}><p>{content}</p>".format(
                    title=news.get("title"),
                    image_src=news.get("image"),
                    content=news.get("content"),
                )
                for news
                in news_list
            ])

        return HttpResponse(
            content,
        )
