# Generated by Django 4.2.4 on 2023-11-27 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_sid', '0012_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='best_sellers',
            field=models.IntegerField(default=0),
        ),
    ]