# Generated by Django 4.1.7 on 2023-04-10 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0024_alter_ordem_serviço_situação'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projetos',
            name='relatorio',
            field=models.CharField(max_length=100),
        ),
    ]