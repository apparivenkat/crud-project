# Generated by Django 3.2.5 on 2022-05-29 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_studentregistration_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentregistration',
            name='course',
            field=models.CharField(choices=[('Computer Science', 'Computer Science'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Electrical Engineering', 'Electrical Engineering'), ('Electronics Engineering', 'Electronics Engineering')], max_length=50),
        ),
        migrations.AlterField(
            model_name='studentregistration',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50),
        ),
    ]
