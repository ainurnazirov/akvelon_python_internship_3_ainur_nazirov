from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=254)

class Transaction(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField(auto_now=False, auto_now_add=False)
