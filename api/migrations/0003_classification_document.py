# Generated by Django 3.1.3 on 2020-11-22 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201122_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='classification',
            name='document',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
