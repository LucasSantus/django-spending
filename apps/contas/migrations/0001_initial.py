# Generated by Django 3.1.8 on 2021-08-25 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, verbose_name='Título')),
                ('description', models.TextField(null=True, verbose_name='Descrição')),
                ('date_generated', models.DateTimeField(auto_now=True, verbose_name='Data da Criação')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, verbose_name='Título')),
                ('description', models.TextField(null=True, verbose_name='Descrição')),
                ('hour_generated', models.DateTimeField(verbose_name='Data da Transação')),
                ('value', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Valor da Transação')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contas.category')),
            ],
            options={
                'verbose_name': 'Transação',
                'verbose_name_plural': 'Transações',
            },
        ),
    ]
