# Generated by Django 2.2.6 on 2019-10-26 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amigo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('nome_mae', models.CharField(max_length=100, verbose_name='Nome da mãe')),
                ('telefone', models.CharField(max_length=10)),
                ('grupo_amigo', models.CharField(choices=[('prédio', 'prédio'), ('escola', 'escola')], max_length=10, verbose_name='Grupo de amigo')),
            ],
        ),
        migrations.CreateModel(
            name='Caixa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(verbose_name='Número')),
                ('etiqueta', models.CharField(max_length=50)),
                ('cor', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Colecao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'coleção',
                'verbose_name_plural': 'coleções',
            },
        ),
    ]
