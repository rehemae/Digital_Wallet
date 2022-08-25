from django.contrib import admin
from.models import Customer ,Wallet,Account,Transaction,Card,Thirdparty,Notifications,Receipt,Loan,Currency,Reward



class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","email","gender","adress","age","nationality","Id_number","phone_number","marital_status","employment","profile_picture", )
    search_fields=("fist_name","last_name","gender","adress","age","nationality","Id_number","phone_number","marital_status","employment","profile_picture")
admin.site.register(Customer,CustomerAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    list_display=("amount","symbol","country_of_origin",)
    search_fields=("amount","symbol")
admin.site.register(Currency,CurrencyAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display=('pin','status','date','amount','customer','balance',)
    search_fields=("amount",'pin')
admin.site.register(Wallet,WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display=('account_number','account_type','balance','name','Wallet',)
    search_fields=("account_number",'account_type')
admin.site.register(Account,AccountAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display=('wallet','transaction_amount','transaction_type','transaction_charge','transaction_date','receipt','orign_account','destination_account',)
    search_fields=("destination_account",'wallet')
admin.site.register(Transaction,TransactionAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display=('date_issued','card_name','card_type','card_number','expire_date','card_status','security_code','wallet','account','issuer',)
    search_fields=(" issuer",'card_name')
admin.site.register(Card,CardAdmin)

class ThirdpartyAdmin(admin.ModelAdmin):
    list_display=('account','name','thirdparty_id','phone_number',)
    search_fields=("account",'name')
admin.site.register(Thirdparty,ThirdpartyAdmin)

class NotificationsAdmin(admin.ModelAdmin):
    list_display=('notifications_id','name','date','status','time','receipt',)
    search_fields=("receipt",'notifications_id')
admin.site.register(Notifications,NotificationsAdmin)

class ReceiptAdmin(admin.ModelAdmin):
    list_display=('receipt_type','receipt_date','receipt_file','total_amount','account_number','transaction',)
    search_fields=("transaction",'receipt_type')
admin.site.register(Receipt,ReceiptAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display=('loan_number','loan_type','date_and_time','interest_rate','wallet' ,'guarantor','pay_due_date','loan_balance',)
    search_fields=("loarn_term",'loan_type')
admin.site.register(Loan,LoanAdmin)

class RewardAdmin(admin.ModelAdmin):
    list_display=('transaction','date_and_time','customer_id','gender','bonus',)
    search_fields=("bonus",'date_and_time')
admin.site.register(Reward,RewardAdmin)



   