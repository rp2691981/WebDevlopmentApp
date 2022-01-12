# Generated by Django 4.0 on 2021-12-30 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManagerApp', '0005_customeritems_orginalcost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('UserId', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('Password', models.CharField(max_length=150)),
                ('Name', models.CharField(max_length=200)),
                ('Phone', models.CharField(max_length=14)),
                ('AdharCard', models.CharField(max_length=60)),
                ('Date', models.DateField(auto_now=True)),
                ('Time', models.TimeField(auto_now=True)),
            ],
        ),
    ]