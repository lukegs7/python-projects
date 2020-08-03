from django.urls import path, re_path
from . import views

# namespace
app_name = 'file_download'

urlpatterns = [
    re_path(r'^download/(?P<file_path>.*)/$', views.file_response_download, name='file_download'),
    re_path(r'^fetch/$', views.fet_file_from_internet, name='file_download'),
]
