from rest_framework import serializers
from products.models import Category, Product, Menu, Establishment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'image']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'price', 'ingredients', 'establishment']


class EstablishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Establishment
        fields = ['name', 'category', 'logo', 'image', 'popular']
