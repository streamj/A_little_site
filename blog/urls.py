from django.conf.urls import patterns, include , url
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = patterns('',
    #url(r'^$', 'blog.views.blog_home', name='blog_home'),
    url(r'^(?P<page>\d+)?/?$', ListView.as_view(
        model=Post,
        paginate_by=5,
    )),
    # individual posts
    url(r'^(?P<pub_date__year>\d{4})/(?P<pub_date__month>\d{1,2})/(?P<slug>[a-zA-Z0-9-]+)/?$', DetailView.as_view(model=Post,))
)
