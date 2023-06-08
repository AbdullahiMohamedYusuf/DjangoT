from django.contrib import admin
from  .models import Shoe, Review, Category, Purchase
# Register your models here.

admin.site.register(Shoe)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Purchase)