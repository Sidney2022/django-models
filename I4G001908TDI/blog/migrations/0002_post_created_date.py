# Generated by Django 4.0.5 on 2022-06-17 12:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Created_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='date published'),
            preserve_default=False,
        ),
    ]
