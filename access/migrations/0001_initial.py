# Generated by Django 4.1 on 2023-11-21 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=225)),
                ('password', models.CharField(max_length=225)),
                ('user_type', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'auth',
            },
        ),
    ]
