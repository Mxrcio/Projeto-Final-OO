# Generated by Django 4.2.3 on 2023-07-17 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0002_restaurante_cardapio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('senha', models.CharField(max_length=128)),
            ],
        ),
    ]
