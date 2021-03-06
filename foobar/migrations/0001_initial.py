# Generated by Django 2.2.9 on 2020-01-08 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
                ('description', models.TextField(max_length=40, verbose_name='Description')),
                ('time', models.CharField(max_length=40, verbose_name='Time')),
                ('authors', models.CharField(max_length=40, verbose_name='Authors')),
                ('realisator', models.CharField(max_length=40, verbose_name='Realisator')),
            ],
        ),
    ]
