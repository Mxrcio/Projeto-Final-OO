# Generated by Django 4.2.3 on 2023-07-21 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0006_funcionario_restaurante_cardapio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardapio',
            name='restaurante',
        ),
        migrations.DeleteModel(
            name='Funcionario',
        ),
        migrations.DeleteModel(
            name='Cardapio',
        ),
        migrations.DeleteModel(
            name='Restaurante',
        ),
    ]
