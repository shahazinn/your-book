# Generated by Django 4.1.3 on 2023-01-21 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksiteapp', '0002_adcontact'),
    ]

    operations = [
        migrations.CreateModel(
            name='itemcart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('totalprice', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
