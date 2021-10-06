from rest_framework import serializers
from hw_1.models import Product, Tag, Review, Category



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






