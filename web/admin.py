from django.contrib import admin
from web.models import Expense, Income, Token

admin.site.register(Expense)
admin.site.register(Income)
admin.site.register(Token)