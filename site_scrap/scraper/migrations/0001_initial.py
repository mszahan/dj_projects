# Generated by Django 5.1.5 on 2025-01-16 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(blank=True, max_length=1000, null=True)),
                ('name', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
