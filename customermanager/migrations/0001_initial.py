# Generated by Django 4.2.7 on 2023-11-23 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salutation', models.CharField(max_length=5)),
                ('surname', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
                ('birthday', models.DateField()),
                ('password', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=10)),
            ],
        ),
    ]
