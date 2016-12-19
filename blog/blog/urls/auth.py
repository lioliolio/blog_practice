from django.conf.urls import url

from blog.views.auth import *


urlpatterns = [
    url(r'login/$', login, name="login"),
    url(r'signup/$', signup, name="signup"),
]
