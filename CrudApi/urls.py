from django.urls import re_path as url
from CrudApi import views 
 
urlpatterns = [ 
    url(r'^api/user$', views.user_list),
    url(r'^api/user/(?P<pk>[0-9]+)$', views.user_detail),
]
