from django.urls import path
from .views import home, articoloDetailView, index_news

app_name="news"
urlpatterns = [
    path('news', home, name='home'),
    path("news/articoli/<int:pk>", articoloDetailView, name="articolo_detail"),
    path('index_news', index_news, name='index_news')
]