# Generated by Django 3.2.8 on 2021-12-14 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerApp', '0004_alter_cusdashboard_bannerimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='cusdashboard',
            name='DishCost',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AddField(
            model_name='cusdashboard',
            name='dishName',
            field=models.CharField(default='none', max_length=300),
        ),
    ]
