# Generated by Django 4.0 on 2022-01-04 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManagerApp', '0006_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chiefmodel',
            name='id',
        ),
        migrations.AlterField(
            model_name='chiefmodel',
            name='UserId',
            field=models.CharField(max_length=300, primary_key=True, serialize=False),
        ),
    ]
