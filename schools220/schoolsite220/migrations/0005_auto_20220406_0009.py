# Generated by Django 3.2.12 on 2022-04-05 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolsite220', '0004_statistics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistics',
            name='classroom',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='science',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='students',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='teachers',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
