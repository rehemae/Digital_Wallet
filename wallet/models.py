import email
from inspect import stack
from locale import currency
from operator import countOf
from django.db import models
from django.utils import timezone

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField (max_length=15,null=True)
    last_name=models.CharField(max_length=15,null=True)
    GENDER_CHOICES=(
       ("M", "Male"),
       ("F", "Female"),
   )
    gender= models.CharField(max_length=1,choices=GENDER_CHOICES,null=True)
    adress=models.CharField(max_length=15,null=True)
    age=models.PositiveSmallIntegerField()
    nationality=models.CharField(max_length=15,null=True)
    Id_number=models.CharField(max_length=15,null=True)
    phone_number=models.CharField(max_length=15,null=True)
    email=models.EmailField(max_length=25,null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/',null=True)


class Currency(models.Model):
   amont=models.IntegerField()
   symbol=models.CharField(max_length=15,null=True)
   country_of_origin=models.CharField(max_length=24,null=True) 


class Wallet(models.Model):
    currency=models.ForeignKey('Currency',on_delete=models.CASCADE,related_name='Wallet_currency')
    customer=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='Wallet_customer')
    balance=models.IntegerField()
    amount=models.IntegerField()
    date=models.DateTimeField(default=timezone.now)
    status=models.CharField(max_length=15,null=True)
    pin=models.TextField(max_length=15,null=True)

class Account(models.Model):
    account_number=models.IntegerField()
    account_type=models.CharField(max_length=15,null=True)
    balance=models.IntegerField() 
    name=models.CharField(max_length=15,null=True) 
    Wallet=models.ForeignKey("Wallet",on_delete=models.CASCADE,related_name='Account_wallet') 


class Transaction(models.Model):
    wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Transaction_wallet') 
    transaction_amount=models.IntegerField() 
    transaction_type=models.IntegerField()
    transaction_type=models.CharField(max_length=15,null=True)
    transaction_charge=models.IntegerField()
    transaction_date=models.DateTimeField(default=timezone.now)
    receipt=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='Transaction_receipt')
    orign_account=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Transaction_orign_account')
    destination_account=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Transaction_destination_account')

class Card(models.Model):
    date_issued=models.DateTimeField(default=timezone.now)
    card_name=models.CharField(max_length=15,null=True)
    card_number=models.IntegerField() 
    card_type=models.CharField(max_length=15,null=True)
    expire_date=models.DateTimeField(default=timezone.now)
    card_status=models.CharField(max_length=15,null=True) 
    security_code=models.IntegerField() 
    wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Card_wallet') 
    account=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Card_account')
    issuer=models.CharField(max_length=15,null=True)

class Thirdparty(models.Model):
    account=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Thirdparty_account')
    name=models.CharField(max_length=15,null=True)
    thirdparty_id=models.IntegerField()
    phone_number=models.IntegerField()

class Notifications(models.Model):
    notifications_id=models.IntegerField() 
    name=models.CharField(max_length=15,null=True)
    status=models.CharField(max_length=15,null=True)
    date=models.DateTimeField(default=timezone.now)
    time=models.DateTimeField(default=timezone.now) 
    receipt=models.ForeignKey('Thirdparty',on_delete=models.CASCADE,related_name='Notifications_receipt')  



class Receipt(models.Model):
    receipt_type=models.CharField(max_length=15,null=True)  
    receipt_date=models.DateTimeField(default=timezone.now) 
    receipt_file=models.FileField() 
    total_amount=models.IntegerField()
    account_number=models.IntegerField()
    transaction=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Receipt_transaction')

class Loan(models.Model):
    loan_number=models.IntegerField() 
    loan_type=models.CharField(max_length=15,null=True)
    amount=models.IntegerField() 
    date_and_time=models.DateTimeField(default=timezone.now)
    wallet=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Loan_wallet') 
    interest_rate=models.IntegerField() 
    guarantor=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='Loan_guarantor')
    pay_due_date=models.DateTimeField(default=timezone.now)
    loan_balance=models.IntegerField()
    loarn_term=models.IntegerField



class Reward(models.Model):
    transaction=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Reward_transaction')
    date_and_time=models.DateTimeField(default=timezone.now)
    customer_id=models.IntegerField()
    GENDER_CHOICES=(
       ("M", "Male"),
       ("F", "Female"),
   )
    gender= models.CharField(max_length=1,choices=GENDER_CHOICES,null=True)
    bonus=models.IntegerField()

        



   
