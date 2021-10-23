# Generated by Django 3.2 on 2021-10-23 17:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user.models.profile_image


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, max_length=128, null=True, upload_to=user.models.profile_image.get_file_path, verbose_name='Image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_image', to=settings.AUTH_USER_MODEL, verbose_name='Avatar')),
            ],
            options={
                'verbose_name': 'ProfileImage',
                'verbose_name_plural': 'ProfileImages',
            },
        ),
    ]
