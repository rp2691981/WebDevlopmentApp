# Generated by Django 4.0 on 2021-12-17 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChiefModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserId', models.CharField(max_length=300)),
                ('Password', models.CharField(max_length=300)),
                ('ChiefName', models.CharField(max_length=300)),
                ('Chief_Experiance', models.CharField(max_length=50)),
                ('C_Post', models.CharField(max_length=50)),
                ('Cheif_AdharCard', models.CharField(max_length=300)),
                ('Chief_Number', models.CharField(max_length=300)),
                ('ChiefAddress', models.CharField(max_length=300)),
                ('ProfileImage', models.FileField(default='None', max_length=600, upload_to='Mainmenu/RiceChapati/')),
                ('Date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
