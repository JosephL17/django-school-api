# Generated by Django 5.0.7 on 2024-07-23 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('student_email', models.EmailField(max_length=254)),
                ('personal_email', models.EmailField(max_length=254)),
                ('locker_number', models.IntegerField(default=1)),
                ('good_student', models.BooleanField()),
            ],
        ),
    ]
