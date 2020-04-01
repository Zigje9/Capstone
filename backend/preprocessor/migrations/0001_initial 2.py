# Generated by Django 3.0.3 on 2020-03-10 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('videoId', models.CharField(max_length=11)),
                ('keyword', models.CharField(max_length=300, null=True)),
                ('model_tag', models.CharField(max_length=300, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
