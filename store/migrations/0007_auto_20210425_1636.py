# Generated by Django 3.2 on 2021-04-25 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_rename_category_order_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='Non', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
