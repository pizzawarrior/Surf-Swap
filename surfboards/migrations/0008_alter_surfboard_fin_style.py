# Generated by Django 4.2.5 on 2023-09-10 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surfboards', '0007_alter_surfboard_fin_style_alter_surfboard_fin_system_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surfboard',
            name='fin_style',
            field=models.CharField(choices=[('Single fin', 'Single'), ('Twin', 'Twin'), ('2+1', '2+1'), ('Thruster', 'Thruster'), ('Quad', 'Quad'), ('Finless', 'Finless'), ('Other', 'Other')], max_length=20, verbose_name='Fin Style'),
        ),
    ]
