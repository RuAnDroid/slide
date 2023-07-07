# Generated by Django 4.2.2 on 2023-07-02 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_firm_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firm',
            name='owner',
        ),
        migrations.AddField(
            model_name='firm',
            name='owner',
            field=models.ManyToManyField(to='shop.projects'),
        ),
    ]