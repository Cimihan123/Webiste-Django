# Generated by Django 3.0.7 on 2020-07-28 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='todo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.Todo'),
        ),
    ]
