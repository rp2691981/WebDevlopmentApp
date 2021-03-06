# Generated by Django 4.0 on 2021-12-14 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerApp', '0009_ricechapati'),
    ]

    operations = [
        migrations.AddField(
            model_name='ricechapati',
            name='CreatedDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='ricechapati',
            name='ItemCost',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AddField(
            model_name='ricechapati',
            name='ItemImage',
            field=models.FileField(default='None', max_length=600, upload_to='Mainmenu/RiceChapati/'),
        ),
        migrations.AddField(
            model_name='ricechapati',
            name='ItemName',
            field=models.CharField(default='enter', max_length=300),
        ),
        migrations.AlterField(
            model_name='ricechapati',
            name='Check',
            field=models.CharField(default='rice', max_length=100),
        ),
    ]
