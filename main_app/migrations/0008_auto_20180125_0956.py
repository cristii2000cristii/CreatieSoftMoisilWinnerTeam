# Generated by Django 2.0.1 on 2018-01-25 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diets',
            name='description',
            field=models.CharField(max_length=600),
        ),
    ]
