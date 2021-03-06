from rest_framework import serializers
from hw_1.models import *
from rest_framework.exceptions import ValidationError




class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductListSerializer(serializers.ModelSerializer):

    category = CategoryListSerializer()

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'category', 'tags', "reviews"]


class ProductsReviewListSerializer(serializers.ModelSerializer):
    reviews = ReviewListSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'reviews']


class ProductsActiveTagsListSerializer(serializers.ModelSerializer):
    activeTags = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = 'id title activeTags'.split()

    def get_activeTags(self, product):
        tags =Tag.objects.filter(product=product).exclude(is_active=False)
        return TagListSerializer(tags, many=True).data


class ProductCreateValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=2, max_length=100)
    description = serializers.CharField(min_length=10)
    price = serializers.IntegerField()
    category = serializers.IntegerField()
    tags = serializers.ListField(child=serializers.IntegerField())





