from django.conf.urls import patterns, include , url
from django.views.generic import ListView
from blog.models import Post

urlpatterns = patterns('',
    #url(r'^$', 'blog.views.blog_home', name='blog_home'),
    url(r'^(?P<page>\d+)?/?$', ListView.as_view(
        model=Post,
        paginate_by=5,
    )),
    # match \d+ to id
    # url(r'^(?P<id>\d+)/$', 'blog.views.detail', name='detail'),
)
