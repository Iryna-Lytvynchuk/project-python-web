# Generated by Django 3.2.7 on 2021-09-05 22:50

from django.db import migrations, models
import storages.backends.sftpstorage


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='contact_photo',
            field=models.FileField(null=True, storage=storages.backends.sftpstorage.SFTPStorage(), upload_to=''),
        ),
    ]
