# Generated by Django 4.0.4 on 2022-05-13 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='feedback',
            field=models.TextField(default='5 Star on trustpilot'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='summary',
            field=models.TextField(default='No Summary Provided'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=25),
        ),
    ]
