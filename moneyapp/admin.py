from django.contrib import admin
from .models import User, Transaction


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email']
    list_display_links = ['id', ]
    search_fields = ['id', 'first_name', 'last_name', 'email']


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'amount', 'date']
    list_display_links = ['id', 'user_id']
    search_fields = ['id', 'user_id', 'amount', 'date']


admin.site.register(User, UserAdmin)
admin.site.register(Transaction, TransactionAdmin)
