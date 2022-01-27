# Generated by Django 3.2.9 on 2021-12-19 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.ImageField(upload_to='categoryimgs/', verbose_name='Kategoriya rasm')),
                ('name', models.CharField(max_length=100, verbose_name='Kategoriya nomi')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='*')),
            ],
        ),
    ]
