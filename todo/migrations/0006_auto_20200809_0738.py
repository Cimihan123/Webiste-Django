# Generated by Django 3.0.7 on 2020-08-09 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20200809_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='image',
            field=models.ImageField(upload_to='todopics'),
        ),
    ]
