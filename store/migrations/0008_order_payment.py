# Generated by Django 3.1.7 on 2021-11-30 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_products_second'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.BooleanField(default=False),
        ),
    ]
