# Generated by Django 4.2.1 on 2023-06-11 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0003_file_contract_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='file',
        ),
    ]