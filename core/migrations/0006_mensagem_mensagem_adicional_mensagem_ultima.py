# Generated by Django 4.2.7 on 2023-11-12 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_mensagem_delete_configuracao'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensagem',
            name='mensagem_adicional',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mensagem',
            name='ultima',
            field=models.BooleanField(default=False),
        ),
    ]
