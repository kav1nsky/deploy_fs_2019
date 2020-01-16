# Generated by Django 3.0.2 on 2020-01-16 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codes', '0003_remove_codesuser_real_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='city',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='full_desc',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='lat',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='lng',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='main_img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='preview_desc',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='preview_img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='timestamp',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
