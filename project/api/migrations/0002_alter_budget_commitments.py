# Generated by Django 4.1.5 on 2023-01-16 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='commitments',
            field=models.IntegerField(),
        ),
    ]
