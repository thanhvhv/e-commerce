from django.contrib import admin
from .models import UserAccount, Product, Category, Order, OderItem, Color, Size, ImageProduct, SubCategory, CardItem

# Register your models here.
admin.site.register(UserAccount)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Order)
admin.site.register(OderItem)
admin.site.register(CardItem)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(ImageProduct)
