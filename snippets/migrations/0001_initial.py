# Generated by Django 2.0.5 on 2018-06-18 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('code', models.CharField(blank=True, default='', max_length=30)),
                ('linenos', models.CharField(blank=True, default='', max_length=30)),
                ('language', models.CharField(blank=True, default='', max_length=30)),
                ('style', models.CharField(blank=True, default='', max_length=30)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
