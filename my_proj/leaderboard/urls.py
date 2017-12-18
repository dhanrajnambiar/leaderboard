from django.urls import re_path, path

from . import views

urlpatterns = [
    path('add', views.add, name = 'add_participant'),
    path('delete', views.delete, name = 'delete_participant'),
    re_path(r'', views.home, name = 'list_participant'),

]
