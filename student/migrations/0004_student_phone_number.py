# Generated by Django 3.0.6 on 2020-05-16 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20200516_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
