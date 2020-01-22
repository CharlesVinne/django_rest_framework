from rest_framework import routers
from produtos.views import ProdutoViewSet
from django.contrib import admin
from vendas.views import VendaViewSet
from django.urls import path, include
from clientes.views import ClienteViewSet

rota = routers.DefaultRouter()
rota.register(r'produtos', ProdutoViewSet)
rota.register(r'vendas', VendaViewSet)
rota.register(r'clientes', ClienteViewSet)


urlpatterns = [
    path(r'api/', include(rota.urls)),
    path('admin/', admin.site.urls),
]
