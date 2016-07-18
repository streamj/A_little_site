from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples
    url(r'^home$', 'lists.views.list_home', name='list_home'),
    url(r'^(\d+)/$','lists.views.view_list', name='view_list'),
    url(r'^new$', 'lists.views.new_list', name='new_list'),
)
