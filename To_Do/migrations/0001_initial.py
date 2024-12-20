# Generated by Django 4.2.3 on 2024-10-02 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('taskTitle', models.CharField(max_length=30)),
                ('taskDescription', models.CharField(max_length=100)),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
    ]
