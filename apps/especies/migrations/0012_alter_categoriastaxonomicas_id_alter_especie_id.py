# Generated by Django 4.0.6 on 2022-07-14 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('especies', '0011_alter_categoriastaxonomicas_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoriastaxonomicas',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='idCategoria'),
        ),
        migrations.AlterField(
            model_name='especie',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='idEspecie'),
        ),
    ]
