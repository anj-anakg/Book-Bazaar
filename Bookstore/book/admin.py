from django.contrib import admin
from .models import Book
from .models import CartItem
from .models import Cart

# Register your models here.

admin.site.register(Book)
admin.site.register(CartItem)
admin.site.register(Cart)
