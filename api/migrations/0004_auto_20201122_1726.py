# Generated by Django 3.1.3 on 2020-11-22 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_classification_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classification',
            name='document',
            field=models.FileField(default='', upload_to='files'),
        ),
    ]