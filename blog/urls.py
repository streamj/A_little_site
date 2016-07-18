from django.conf.urls import patterns, include , url

urlpatterns = patterns('',
    url(r'^home$', 'blog.views.blog_home', name='blog_home'),
)
