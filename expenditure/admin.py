from django.contrib import admin
from expenditure.models import Category, Budget, Expenditure, Transaction
# Register your models here.
admin.site.register(Category)
admin.site.register(Budget)
admin.site.register(Expenditure)
admin.site.register(Transaction)


