# Generated by Django 3.2.12 on 2022-03-11 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0003_auto_20220311_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='needitem',
            name='todo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='need_items', to='meal.todo'),
        ),
    ]
