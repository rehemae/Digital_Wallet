from django.contrib import admin
from.models import Customer,Wallet,Account,Transaction,Card,Thirdparty,Notifications,Receipt,Loan,Currency,Reward


class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","email",)
    search_fields=("fist_name","last_name")
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Currency)
admin.site.register(Wallet)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Card)
admin.site.register(Thirdparty)
admin.site.register(Notifications)
admin.site.register(Receipt)
admin.site.register(Loan)
admin.site.register(Reward)


   