# Generated by Django 4.0 on 2021-12-13 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SweetCornerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DessertType', models.CharField(max_length=200)),
                ('DessertName', models.CharField(max_length=200)),
                ('DessertCost', models.CharField(max_length=200)),
                ('DessertImage', models.FileField(max_length=600, upload_to='Dessert/')),
            ],
        ),
    ]