from reference.urls import *

import views

urlpatterns = patterns('',
                       url(r'^$', views.list, name='list'),
                       url(r'^upload/$', views.upload_file, name='upload'),
                       url(r'^upload_view/$', views.upload_view, name='upload_view'),
                       url(r'^(?P<doc_id>\d+)/$', views.law_detail, name='law'),
)
