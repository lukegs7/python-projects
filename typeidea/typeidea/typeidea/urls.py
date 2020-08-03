from django.contrib import admin
from django.urls import path,include
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('admin/',admin.site.urls),
    path('auth-api/',include('rest_framework.urls')),
    path('docs/',include_docs_urls(title='接口框架')),
    path('api/',include('comment.urls'))
]
