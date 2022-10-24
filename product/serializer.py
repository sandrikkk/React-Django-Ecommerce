from rest_framework import serializers
from product.models import StoreProductsModel

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreProductsModel
        fields = ['_id', 'user','product_name', 'price','description', 'get_image', 'get_thumbnail', 'get_absolute_url', 'countInStock', 'rating']
