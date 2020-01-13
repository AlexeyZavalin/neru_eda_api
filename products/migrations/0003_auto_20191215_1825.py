# Generated by Django 3.0 on 2019-12-15 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20191215_0520'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='products.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ingredients',
            field=models.TextField(blank=True, max_length=256, null=True, verbose_name='Ингредиенты'),
        ),
    ]