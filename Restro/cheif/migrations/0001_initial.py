# Generated by Django 4.0 on 2022-01-11 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ManagerApp', '0008_recordsmanger_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheifFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dishname', models.CharField(max_length=200)),
                ('quantity', models.CharField(max_length=20)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ManagerApp.recordsmanger')),
            ],
        ),
    ]
