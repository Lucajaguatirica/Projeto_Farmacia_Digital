# Generated by Django 3.2.9 on 2021-12-01 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_receita_medicacoes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receita',
            name='medicacoes',
        ),
        migrations.DeleteModel(
            name='Horario',
        ),
        migrations.DeleteModel(
            name='receita',
        ),
    ]