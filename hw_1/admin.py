from django.contrib import admin
from .models import Category, Product, Review, Tag
# Register your models here.


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Review)
