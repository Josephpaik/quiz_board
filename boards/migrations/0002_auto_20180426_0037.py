# Generated by Django 2.0.4 on 2018-04-25 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='last_update',
            new_name='last_updated',
        ),
        migrations.AddField(
            model_name='topic',
            name='view',
            field=models.PositiveIntegerField(default=0),
        ),
    ]