# Generated by Django 4.2.7 on 2023-11-12 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_mensagem_video_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensagem',
            name='video_url',
        ),
    ]
