# Generated by Django 5.1 on 2024-09-11 00:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_clientcontactsmodel_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientcontactsmodel',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.clientsmodel'),
            preserve_default=False,
        ),
    ]
