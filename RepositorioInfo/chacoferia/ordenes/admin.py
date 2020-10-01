from django.contrib import admin
from .models import OrderLine, Order

# Register your models here.

admin.site.register([Order, OrderLine])