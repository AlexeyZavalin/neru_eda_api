from django.urls import include, path
from rest_framework import routers
from products import views as product_views

router = routers.DefaultRouter()
router.register(r'categories', product_views.CategoriesViewSet)
router.register(r'products', product_views.ProductsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework'))
]
