# Generated by Django 3.1.7 on 2021-04-11 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210411_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='prod_id',
        ),
        migrations.AddField(
            model_name='product',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
