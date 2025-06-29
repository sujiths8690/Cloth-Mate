# Generated by Django 5.2.1 on 2025-05-24 17:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.CharField(max_length=100)),
                ('category_name', models.CharField(max_length=100)),
                ('dress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.dress')),
            ],
            options={
                'db_table': 'category',
            },
        ),
    ]
