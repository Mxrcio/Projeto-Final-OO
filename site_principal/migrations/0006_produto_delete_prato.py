# Generated by Django 4.2.3 on 2023-07-20 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_principal', '0005_rename_cartitem_pedido'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.DeleteModel(
            name='Prato',
        ),
    ]
