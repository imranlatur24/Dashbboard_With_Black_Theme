# Generated by Django 3.2.6 on 2021-12-02 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20211130_2135'),
    ]

    operations = [
        migrations.CreateModel(
            name='new_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('X', models.CharField(max_length=100)),
                ('Y', models.CharField(max_length=100)),
            ],
        ),
    ]
