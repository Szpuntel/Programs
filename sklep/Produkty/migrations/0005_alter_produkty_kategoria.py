# Generated by Django 4.0.5 on 2022-07-01 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0004_kategoria_produkty_kategoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkty',
            name='kategoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Produkty.kategoria'),
        ),
    ]
