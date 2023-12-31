# Generated by Django 4.2.5 on 2023-09-10 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surfboards', '0003_alter_surfboard_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surfboard',
            name='fin_style',
            field=models.CharField(choices=[('single fin', 'Single'), ('twin', 'Twin'), ('thruster', 'Thruster'), ('quad', 'Quad'), ('finless', 'Finless'), ('other', 'Other')], max_length=20, verbose_name='Fin Style'),
        ),
        migrations.AlterField(
            model_name='surfboard',
            name='fin_system',
            field=models.CharField(choices=[('fcs1', 'FCS 1'), ('fcs2', 'FCS 2'), ('futures', 'Futures'), ('other', 'Other')], max_length=20, verbose_name='Fin System'),
        ),
        migrations.AlterField(
            model_name='surfboard',
            name='style',
            field=models.CharField(choices=[('fish', 'Fish'), ('twin', 'Twin'), ('round', 'Round'), ('asym', 'Asym'), ('performance', 'Performance'), ('swallow-tail', 'Swallow-tail'), ('pin tail', 'Pin tail'), ('squash', 'Squash'), ('mini-simmons', 'Mini-simmons'), ('other', 'Other')], max_length=100, verbose_name='Board Style'),
        ),
        migrations.AlterField(
            model_name='surfboard',
            name='type',
            field=models.CharField(choices=[('shortboard', 'Shortboard'), ('mid-length', 'Mid-length'), ('longboard', 'Longboard')], max_length=20, verbose_name='Board Type'),
        ),
    ]
