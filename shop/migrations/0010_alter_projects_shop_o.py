# Generated by Django 4.2.2 on 2023-07-04 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_projects_options_alter_projects_shop_o'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='shop_o',
            field=models.CharField(default='https://www.ozon.ru/seller/ip-valyan-a-n-675330/products/?miniapp=seller_675330', editable=False, max_length=200),
        ),
    ]
