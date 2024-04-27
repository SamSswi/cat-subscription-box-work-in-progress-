from django.contrib import admin
from .models import UserProfile, Order, Product, OrderLine, SubscriptionPlan, Subscription

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(OrderLine)
admin.site.register(SubscriptionPlan)
admin.site.register(Subscription)
