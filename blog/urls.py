from django.conf.urls import include, url

from . import views

"""
Atribuímos uma view chamada post_list para ^ $ URL. Essa expressão regular corresponderá a ^ (um começo) seguido por $ 
(fim) - então somente uma seqüência vazia irá corresponder. E isso é correto, porque em resolvedores de Django url, 
' http://127.0.0.1:8000 /' não é uma parte da URL. Este padrão irá mostrar o Django que views.post_list é o lugar certo 
para ir, se alguém entra em seu site no endereço 'http://127.0.0.1:8000 /'.
"""

urlpatterns = [
	url(r'^$', views.post_list),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]