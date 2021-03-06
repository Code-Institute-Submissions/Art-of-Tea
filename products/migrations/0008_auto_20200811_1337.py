# Generated by Django 3.0.7 on 2020-08-11 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200809_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_gallery',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.DeleteModel(
            name='ImageGallery',
        ),
    ]
