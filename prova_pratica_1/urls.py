from django.urls import path
from prova_pratica_1.views import index_prova_pratica_1, differenza, pari

app_name="prova_pratica_1"
urlpatterns=[
    path('index_prova_pratica_1', index_prova_pratica_1, name='index_prova_pratica_1'),
    path('differenza', differenza, name='differenza'),
    path('pari', pari, name='pari')
]
