# Generated by Django 4.2.7 on 2023-12-31 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('number', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=20)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
