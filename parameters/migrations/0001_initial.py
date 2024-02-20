# Generated by Django 5.0.1 on 2024-02-20 10:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compID', models.CharField(blank=True, max_length=100)),
                ('parameter1', models.CharField(blank=True, max_length=100)),
                ('parameter2', models.CharField(blank=True, max_length=100)),
                ('parameter3', models.CharField(blank=True, max_length=100)),
                ('parameter4', models.CharField(blank=True, max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
