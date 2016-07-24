from django.conf.urls import include , url
from . import views

urlpatterns = [
    #url(r'^$', 'blog.views.blog_home', name='blog_home'),
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail, name='post_detail')
]
