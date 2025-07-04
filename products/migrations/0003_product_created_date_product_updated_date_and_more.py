# Generated by Django 5.2 on 2025-05-24 13:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_category_remove_product_author_product_catagory'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(choices=[('for_kids', 'For Kids'), ('for_men', 'For Men'), ('for_women', 'For women')], max_length=120),
        ),
    ]
