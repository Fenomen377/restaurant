# Generated by Django 4.1.2 on 2022-10-31 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodanddrinks',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='menu.category', verbose_name='Категория'),
        ),
    ]
