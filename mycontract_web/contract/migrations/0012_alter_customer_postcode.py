# Generated by Django 4.2.1 on 2023-06-14 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0011_alter_log_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='postcode',
            field=models.CharField(max_length=50),
        ),
    ]