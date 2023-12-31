# Generated by Django 4.2.5 on 2023-09-09 23:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Surfboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('model', models.TextField(max_length=100, null=True)),
                ('type', models.CharField(max_length=25)),
                ('length', models.DecimalField(decimal_places=2, max_digits=6)),
                ('width', models.DecimalField(decimal_places=2, max_digits=5)),
                ('thickness', models.DecimalField(decimal_places=2, max_digits=3)),
                ('volume', models.DecimalField(decimal_places=2, max_digits=3)),
                ('style', models.CharField(max_length=100)),
                ('fin_style', models.CharField(max_length=50)),
                ('fin_system', models.CharField(max_length=50)),
                ('image', models.URLField(blank=True)),
                ('currently_available', models.BooleanField(default=False)),
                ('description', models.CharField(max_length=1000)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='surfboards', to=settings.AUTH_USER_MODEL)),
                ('reservation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='surfboards', to='surfboards.reservation')),
            ],
        ),
    ]
