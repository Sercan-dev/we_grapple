# Generated by Django 2.1.5 on 2020-01-02 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='image',
            field=models.ImageField(blank=True, default='media/', null=True, upload_to=''),
        ),
    ]
