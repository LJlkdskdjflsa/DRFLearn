# Generated by Django 3.0.5 on 2021-06-08 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_auto_20210608_0804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.AlterField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
