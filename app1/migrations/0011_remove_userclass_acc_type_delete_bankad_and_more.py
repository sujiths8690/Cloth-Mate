# Generated by Django 5.2.1 on 2025-05-31 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userclass',
            name='acc_type',
        ),
        migrations.DeleteModel(
            name='BankAd',
        ),
        migrations.DeleteModel(
            name='AccountType',
        ),
        migrations.DeleteModel(
            name='UserClass',
        ),
    ]
