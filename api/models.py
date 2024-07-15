from django.db import models
from django.contrib.auth.models import User

class Expence(models.Model):
    
    title=models.CharField(max_length=200)
    
    amount=models.PositiveIntegerField()
    
    expence_categories=(
        ('Housing','Housing'),
        ('Transportation','Transportation'),
        ('Food','Food'),
        ('Health','Health'),
        ('Entertainment','Entertainment'),
        ('Debtpayments','Debtpayments'),
        ('personalcare','personalcare'),
        ('Education','Education'),
        ('Savings','Savings'),
        ('Miscellaneous','Miscellaneous')
    )
    
    category=models.CharField(max_length=200,choices=expence_categories,default='Miscellaneous')
    
    priority_optoins=(
        ('Need','Need'),
        ('Want','Want')
    )
    
    priority=models.CharField(max_length=200,choices=priority_optoins,default='Need')
    
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    
    created_date=models.DateTimeField(auto_now_add=True)
    
    updated_date=models.DateTimeField(auto_now=True)
    
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
    
        return self.title
    

class Income(models.Model):
    
    title=models.CharField(max_length=200)
    amount=models.PositiveIntegerField()
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    income_categories=(
        ('Salary','Salary'),
        ('Business','Business'),
        ('Investment','Investment'),
        ('Rental','Rental'),
        ('Interest','Interest'),
        ('Dividend','Dividend'),
        ('Capital','Capital'),
        ('Pension','Pension'),
        ('Social Security','Social Security'),
        ('Royality','Royality')
    )
    category=models.CharField(max_length=200,choices=income_categories,default='Salary')
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


