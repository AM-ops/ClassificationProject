# Generated by Django 3.1.3 on 2020-11-22 11:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classification',
            options={'ordering': ['file_name']},
        ),
        migrations.RemoveField(
            model_name='classification',
            name='description',
        ),
        migrations.RemoveField(
            model_name='classification',
            name='name',
        ),
        migrations.AddField(
            model_name='classification',
            name='file_description',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='classification',
            name='file_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='classification',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='classification',
            name='file_type',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='classificationitem',
            name='item_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.RemoveField(
            model_name='classificationitem',
            name='item_type',
        ),
        migrations.AddField(
            model_name='classificationitem',
            name='item_type',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.classification'),
        ),
    ]
