# Generated by Django 4.2.1 on 2023-05-24 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spend', '0010_spend_creation_alter_spend_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spend',
            name='Creation',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]