# Generated by Django 3.2.12 on 2022-04-06 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolsite220', '0013_auto_20220406_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='gallery')),
            ],
            options={
                'verbose_name': 'gallery',
                'verbose_name_plural': 'galleries',
            },
        ),
    ]
