from django.conf.urls import url, include
from django.contrib import admin

from blog.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', home, name="home"),
    url(r'^about/$', about, name="about"),
    url(r'^rooms/(?P<room_id>\d+)/$', room, name="room"),
    url(r'^news/$', news, name="news"),

    url(r'^posts/$', list, name="post-list"),
    url(r'^posts/(?P<post_id>\d+)/$', detail, name="post-detail"),
    url(r'^posts/new/$', new, name="post-new"),
    url(r'^posts/create/$', create, name="post-create"),
    url(r'^posts/(?P<post_id>\d+)/edit/$', edit, name="post-edit"),
    url(r'^posts/(?P<post_id>\d+)/update/$', update, name="post-update"),
    url(r'^posts/(?P<post_id>\d+)/delete/$', delete, name="post-delete"),

    url(r'^naver/posts$', naver_posts_list, name="naver-posts-list"),

    url(r'^policy/', include("blog.urls.policy", namespace="policy")),
]
