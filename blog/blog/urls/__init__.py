from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin

from blog.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^about/$', about, name="about"),
    url(r'^rooms/(?P<room_id>\d+)/$', room, name="room"),
    url(r'^news/$', news, name="news"),
    url(r'^pricing/$', PricingView.as_view(), name="pricing"),

    url(r'^posts/', include("blog.urls.posts", namespace="posts")),
    url(r'^policy/', include("blog.urls.policy", namespace="policy")),
    url(r'^', include("blog.urls.auth", namespace="auth")),

    url(r'^naver/posts$', naver_posts_list, name="naver-posts-list"),

    url(r'^policy/', include("blog.urls.policy", namespace="policy")),

    url(r'^bitly/', include("blog.urls.bitly", namespace="bitly")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
