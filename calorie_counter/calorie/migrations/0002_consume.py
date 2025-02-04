# Generated by Django 5.1.5 on 2025-01-18 05:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calorie', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Consume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_consume', to='calorie.food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_consume', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
