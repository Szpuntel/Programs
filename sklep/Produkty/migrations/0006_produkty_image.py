# Generated by Django 4.0.5 on 2022-07-02 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0005_alter_produkty_kategoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='produkty',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='product_pics'),
        ),
    ]
