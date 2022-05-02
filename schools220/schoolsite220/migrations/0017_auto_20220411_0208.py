# Generated by Django 3.2.12 on 2022-04-10 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schoolsite220', '0016_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutschool',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='aboutschool',
            name='describtions',
            field=models.TextField(verbose_name='descriptions'),
        ),
        migrations.AlterField(
            model_name='aboutschool',
            name='image',
            field=models.ImageField(blank=True, upload_to='aboutschool', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='aboutschool',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='author',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='schoolsite220.staff', verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='descriptions',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='descriptions'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(upload_to='banner', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='title',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='account',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='account'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='fullname',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='fullname'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='phone_number'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='text',
            field=models.TextField(verbose_name='text'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='course_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='course_name'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='day',
            field=models.CharField(max_length=19, verbose_name='day'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='description',
            field=models.TextField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='fullname',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='fullname'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='price',
            field=models.FloatField(verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='short_description',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='short_description'),
        ),
        migrations.AlterField(
            model_name='features',
            name='descriptions',
            field=models.TextField(verbose_name='descriptions'),
        ),
        migrations.AlterField(
            model_name='features',
            name='image',
            field=models.ImageField(upload_to='features', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='features',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='gallery', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='managements',
            name='biografy',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='biografy'),
        ),
        migrations.AlterField(
            model_name='managements',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='managements',
            name='fullname',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='fullname'),
        ),
        migrations.AlterField(
            model_name='managements',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='managements', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='managements',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='phone_number'),
        ),
        migrations.AlterField(
            model_name='managements',
            name='pozitions',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='pozitions'),
        ),
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='news',
            name='descriptions',
            field=models.TextField(blank=True, max_length=10000, null=True, verbose_name='descriptions'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='news',
            name='short_descriptions',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='short_descriptions'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='biografy',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='biografy'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='fullname',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='fullname'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='managements', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='phone_number'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='pozitions',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='pozitions'),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='classroom',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='classroom'),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='science',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='science'),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='students',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='students'),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='teachers',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='teachers'),
        ),
        migrations.AlterField(
            model_name='students',
            name='content',
            field=models.TextField(verbose_name='contact'),
        ),
        migrations.AlterField(
            model_name='students',
            name='fullname',
            field=models.CharField(max_length=50, verbose_name='fullname'),
        ),
        migrations.AlterField(
            model_name='students',
            name='image',
            field=models.ImageField(upload_to='students', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='students',
            name='title',
            field=models.CharField(max_length=50, verbose_name='title'),
        ),
    ]