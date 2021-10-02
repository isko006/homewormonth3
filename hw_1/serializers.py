from rest_framework import serializers
from hw_1.models import Product




class ProductListSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'id title description'.split()




