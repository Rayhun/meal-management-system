# Generated by Django 3.2.12 on 2022-03-28 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0006_auto_20220316_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='education',
            name='subject',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='skill',
            name='type',
            field=models.CharField(choices=[('1', 'Beginner'), ('2', 'Intermediate'), ('3', 'Advanced')], default='3', max_length=1),
        ),
    ]
