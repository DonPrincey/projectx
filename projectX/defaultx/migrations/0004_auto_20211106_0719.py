# Generated by Django 3.2.7 on 2021-11-06 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defaultx', '0003_uploadproduct_02'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadcategories',
            name='feature',
            field=models.CharField(max_length=100, verbose_name='Feature Category'),
        ),
        migrations.AlterField(
            model_name='uploadcategories',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Category Name'),
        ),
    ]
