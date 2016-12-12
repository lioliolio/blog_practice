from django.conf.urls import url, include
from django.contrib import admin

from blog.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', home, name="home"),
    url(r'^about/$', about, name="about"),
    url(r'^rooms/(?P<room_id>\d+)/$', room, name="room"),
    url(r'^news/$', news, name="news"),

    url(r'^posts/', include("blog.urls.posts", namespace="posts")),

    url(r'^naver/posts$', naver_posts_list, name="naver-posts-list"),

    url(r'^policy/', include("blog.urls.policy", namespace="policy")),
]
