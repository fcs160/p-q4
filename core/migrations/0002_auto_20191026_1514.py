# Generated by Django 2.2.5 on 2019-10-26 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amigo',
            options={'verbose_name': 'Amigo', 'verbose_name_plural': 'Amigos'},
        ),
        migrations.AlterField(
            model_name='amigo',
            name='telefone',
            field=models.CharField(max_length=16),
        ),
        migrations.CreateModel(
            name='Revista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_edicao', models.IntegerField(verbose_name='Número da edição')),
                ('ano', models.IntegerField(verbose_name='Ano de publicação')),
                ('caixa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Caixa')),
                ('colecao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Colecao')),
            ],
        ),
    ]
