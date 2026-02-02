from django.urls import path
from .views import home, articoloDetailView, index_news, listaArticoli, queryBase, giornalistaDetailView

app_name="news"
urlpatterns = [
    path('news', home, name='home'),
    path("news/articoli/<int:pk>", articoloDetailView, name="articolo_detail"),
    path('index_news', index_news, name='index_news'),
    path('lista_articoli', listaArticoli, name='lista_articoli'),
    #path('lista_articoli/<int:pk>', listaArticoli, name='lista_articoli')
    path('query', queryBase, name='query'),
    path("giornalista/<int:pk>", giornalistaDetailView, name="giornalista_detail")
]