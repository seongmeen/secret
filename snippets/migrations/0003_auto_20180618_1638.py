# Generated by Django 2.0.5 on 2018-06-18 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_auto_20180618_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='highlighted',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='snippets', to=settings.AUTH_USER_MODEL),
        ),
    ]
