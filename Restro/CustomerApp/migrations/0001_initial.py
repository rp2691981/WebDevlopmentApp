# Generated by Django 4.0 on 2021-12-13 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BeveragesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Brand', models.CharField(default='Local', max_length=200)),
                ('DrinkName', models.CharField(max_length=200)),
                ('DrinkType', models.CharField(max_length=200)),
                ('DrinkCost', models.CharField(max_length=200)),
                ('DrinkImage', models.FileField(max_length=600, upload_to='Beverages/')),
            ],
        ),
    ]