# Generated by Django 5.1 on 2024-09-03 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='leader2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('points', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='leader',
        ),
    ]
