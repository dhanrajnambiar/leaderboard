from django.urls import re_path, path, include

from . import views

urlpatterns = [
    path('register', views.register, name = 'create_user'),

    re_path(r'^home/(?P<username>\w+)/',
    include([path('add',views.add_participant, name = 'add_participant'),
    path('delete', views.delete_participant, name = 'delete_participant'),
    re_path(r'',views.user_home, name = 'user_home')])),

    path('login', views.user_login, name = "user_login"),
    path('logout', views.user_logout, name = "user_logout"),
    re_path(r'', views.home, name = 'list_participant'),
]
