# Generated by Django 4.1.7 on 2023-03-09 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_accounts_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='groups',
            field=models.JSONField(),
        ),
    ]
