# Generated by Django 3.2.12 on 2022-05-01 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_committee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatisticalCouncil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('board_structure', models.TextField()),
                ('board_charter', models.TextField()),
            ],
            options={
                'verbose_name': 'statistical_council',
                'verbose_name_plural': 'statistical_councils',
            },
        ),
    ]
