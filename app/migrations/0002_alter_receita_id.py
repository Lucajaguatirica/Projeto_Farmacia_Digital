# Generated by Django 3.2.9 on 2021-11-30 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]