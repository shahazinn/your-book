# Generated by Django 4.1.3 on 2022-11-21 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0002_bitdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='prodb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(blank=True, max_length=30, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile')),
                ('desc', models.CharField(blank=True, max_length=30, null=True)),
                ('proname', models.CharField(blank=True, max_length=30, null=True)),
                ('qua', models.IntegerField(blank=True, null=True)),
                ('pri', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
