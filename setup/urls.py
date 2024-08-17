from django.contrib import admin
from django.urls import path, include
from apps.ecommerce.views import ClienteViewSet, CompraViewSet, ProdutoViewSet, VendedorViewSet, CompraClienteList
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cliente', ClienteViewSet, basename='cliente')
router.register('vendedor', VendedorViewSet, basename='vendedor')
router.register('compra', CompraViewSet, basename='compra')
router.register('produto', ProdutoViewSet, basename='produto')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/cliente/<int:pk>/compra', CompraClienteList.as_view()),
]
