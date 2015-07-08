from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')), #Vai importar blog.urls para a url principal ('')
]									#O Django agora irá redirecionar tudo o que entra em 'http://127.0.0.1:8000 /'para blog.urls e procurar por novas instruções lá
