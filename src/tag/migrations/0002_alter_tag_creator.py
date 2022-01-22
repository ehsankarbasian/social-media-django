# Generated by Django 3.2 on 2022-01-14 17:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
    ]