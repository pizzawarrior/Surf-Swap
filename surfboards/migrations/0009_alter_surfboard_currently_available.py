# Generated by Django 4.2.5 on 2023-09-10 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surfboards', '0008_alter_surfboard_fin_style'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surfboard',
            name='currently_available',
            field=models.BooleanField(default=True),
        ),
    ]