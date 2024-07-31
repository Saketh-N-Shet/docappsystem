# Generated by Django 57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0006_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date_of_appointment',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time_of_appointment',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(2, 'doc'), (1, 'admin'), (3, 'User')], default=1, max_length=50),
        ),
    ]