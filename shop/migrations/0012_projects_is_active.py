# Generated by Django 4.2.2 on 2023-07-05 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_remove_firm_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
