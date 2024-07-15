# Generated by Django 5.0.6 on 2024-06-03 13:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Expence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('amount', models.PositiveIntegerField()),
                ('category', models.CharField(choices=[('Housing', 'Housing'), ('Transportation', 'Transportation'), ('Food', 'Food'), ('Health', 'Health'), ('Entertainment', 'Entertainment'), ('Debtpayments', 'Debtpayments'), ('personalcare', 'personalcare'), ('Education', 'Education'), ('Savings', 'Savings'), ('Miscellaneous', 'Miscellaneous')], default='Miscellaneous', max_length=200)),
                ('priority', models.CharField(choices=[('Need', 'Need'), ('Want', 'Want')], default='Need', max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('Owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('amount', models.PositiveIntegerField()),
                ('category', models.CharField(choices=[('Salary', 'Salary'), ('Business', 'Business'), ('Investment', 'Investment'), ('Rental', 'Rental'), ('Interest', 'Interest'), ('Dividend', 'Dividend'), ('Capital', 'Capital'), ('Pension', 'Pension'), ('Social Security', 'Social Security'), ('Royality', 'Royality')], default='Salary', max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
