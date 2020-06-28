# Generated by Django 2.2.6 on 2019-12-22 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0001_initial'),
        ('roles', '0001_initial'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='department',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='salary',
        ),
        migrations.AddField(
            model_name='employee',
            name='department_name',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='departments.Department'),
        ),
        migrations.AddField(
            model_name='employee',
            name='role_name',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='roles.Role'),
        ),
    ]
