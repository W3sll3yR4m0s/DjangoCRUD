# Generated by Django 3.2.5 on 2022-01-16 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Modelo', models.CharField(max_length=150)),
                ('Marca', models.CharField(max_length=100)),
                ('Ano', models.IntegerField()),
            ],
        ),
    ]
