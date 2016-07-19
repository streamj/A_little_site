from django.conf.urls import patterns, include , url

urlpatterns = patterns('',
    url(r'^home$', 'blog.views.blog_home', name='blog_home'),
    # match \d+ to args
   # url(r'^(?P<args>\d+)/$', 'blog.views.detail', name='detail'),
)
