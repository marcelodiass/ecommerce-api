# Generated by Django 5.1 on 2024-08-17 01:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8)),
                ('descricao', models.TextField(max_length=700)),
                ('categoria', models.CharField(choices=[('ET', 'Eletrônicos'), ('MO', 'Móveis'), ('MD', 'Moda'), ('AL', 'Alimentos'), ('VS', 'Vestuário'), ('OT', 'Outros')], default='OT', max_length=2)),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.vendedor')),
            ],
        ),
    ]
