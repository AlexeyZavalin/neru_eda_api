from rest_framework import viewsets, generics
from products.models import Category, Product, Menu, Establishment
from products.serializers import CategorySerializer, ProductSerializer, EstablishmentSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class EstablishmentsViewSet(viewsets.ModelViewSet):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer


class ProductsList(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        if 'category' in self.kwargs:
            category = self.kwargs['category']
            queryset = Product.objects.filter(category__title=category)
        return queryset