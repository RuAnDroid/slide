# Generated by Django 4.2.2 on 2023-07-03 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_remove_firm_shop_o_remove_firm_social_instagram_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='shop_o',
            field=models.CharField(default='https://www.ozon.ru/seller/ip-valyan-a-n-675330/products/?miniapp=seller_675330', editable=False, max_length=200),
        ),
    ]
