# Generated by Django 4.1.4 on 2023-01-01 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_remove_cartitem_total_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='isOrder',
            field=models.BooleanField(default=False),
        ),
    ]