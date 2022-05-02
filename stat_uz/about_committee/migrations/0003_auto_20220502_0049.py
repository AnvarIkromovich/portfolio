# Generated by Django 3.2.12 on 2022-05-01 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_committee', '0002_statisticalcouncil'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicCouncil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('text1', models.TextField()),
                ('text2', models.TextField()),
                ('text3', models.TextField()),
                ('text4', models.TextField()),
                ('text5', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='statisticalcouncil',
            name='board_charter',
            field=models.TextField(verbose_name='board_charter'),
        ),
        migrations.AlterField(
            model_name='statisticalcouncil',
            name='board_structure',
            field=models.TextField(verbose_name='board_structure'),
        ),
        migrations.AlterField(
            model_name='statisticalcouncil',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='title'),
        ),
    ]
