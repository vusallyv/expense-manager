from django.contrib import admin

from expense.models import Expense


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'date', 'category', 'user')
    list_filter = ('category', 'date')
    search_fields = ('title', 'category')


admin.site.register(Expense, ExpenseAdmin)
