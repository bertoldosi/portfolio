from django.urls import path

from portfolio_App.views import *
from django.conf.urls.static import static

from portfolio_Project import settings

urlpatterns = [
    path('', credenciais, name='credenciais'),
    path('index', index, name='index'),
    path('blog/<id>', blog, name='blog'),
    path('sucesso', successView, name='sucesso'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # NECESSÁRIO PARA AS IMAGENS DO POST
