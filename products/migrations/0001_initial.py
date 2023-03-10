# Generated by Django 4.1.4 on 2022-12-21 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='static/ptoducts')),
                ('price', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('stock', models.IntegerField(default=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categoty')),
            ],
        ),
    ]
