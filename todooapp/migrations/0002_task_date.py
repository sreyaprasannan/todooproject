# Generated by Django 3.2.18 on 2023-05-21 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todooapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2002-05-26'),
            preserve_default=False,
        ),
    ]
