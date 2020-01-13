from django.urls import include, path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from products import views as product_views

router = routers.DefaultRouter()
router.register(r'categories', product_views.CategoriesViewSet)
router.register(r'products', product_views.ProductsViewSet)
router.register(r'establishments', product_views.EstablishmentsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('products/<str:category>', product_views.ProductsList.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
