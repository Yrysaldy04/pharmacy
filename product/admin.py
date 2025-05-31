from django.contrib import admin

# Register your models here.
from .models import Category, Catalog, Question, News, Basket, Sale, Delivery, Organization, Invoice 

# Добавление модели на главную страницу интерфейса администратора
admin.site.register(Category)
admin.site.register(Catalog)
admin.site.register(Question)
admin.site.register(News)
admin.site.register(Basket)
admin.site.register(Sale)
admin.site.register(Delivery)
admin.site.register(Organization)
admin.site.register(Invoice)

