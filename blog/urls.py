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
]