# Generated by Django 4.2.2 on 2023-07-02 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_remove_firm_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='firm',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.projects'),
        ),
    ]
