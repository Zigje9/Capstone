# Generated by Django 3.0.3 on 2020-03-25 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('videoId', models.CharField(max_length=11)),
                ('keyword', models.CharField(max_length=300, null=True)),
                ('startTime', models.IntegerField()),
                ('endTime', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('clip_complete', models.CharField(default='loading', max_length=50)),
            ],
        ),
    ]
