# Generated by Django 5.0 on 2025-01-20 14:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandir', '0004_blogs_event_mission_vision_notice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='content_id',
            field=models.ForeignKey(db_column='content_db', on_delete=django.db.models.deletion.CASCADE, to='mandir.content'),
        ),
    ]
