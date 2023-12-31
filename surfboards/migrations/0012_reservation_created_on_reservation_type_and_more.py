# Generated by Django 4.2.5 on 2023-09-12 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('surfboards', '0011_alter_surfboard_fin_style'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='type',
            field=models.CharField(choices=[('2 weeks', '2 weeks'), ('1 month', '1 month'), ('Other', 'Other')], default=django.utils.timezone.now, max_length=100, verbose_name='Reservation Length'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reservation',
            name='borrower',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to=settings.AUTH_USER_MODEL),
        ),
    ]
