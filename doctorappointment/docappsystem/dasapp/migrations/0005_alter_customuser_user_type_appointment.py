# Generated by Django 

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0004_alter_customuser_user_type_doctorreg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(2, 'doc'), (1, 'admin'), (3, 'User')], default=1, max_length=50),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointmentnumber', models.IntegerField(default=0)),
                ('fullname', models.CharField(max_length=250)),
                ('mobilenumber', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('date_of_appointment', models.DateField()),
                ('time_of_appointment', models.TimeField()),
                ('additional_msg', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dasapp.doctorreg')),
            ],
        ),
    ]