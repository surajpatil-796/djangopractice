# Generated by Django 2.2.6 on 2019-12-03 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=50)),
                ('gmail', models.EmailField(max_length=50)),
                ('address', models.CharField(max_length=50, null=True)),
                ('designation', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('descript', models.CharField(max_length=50)),
                ('emp_name', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='onetoone.Employees')),
            ],
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('descriptt', models.CharField(max_length=50)),
                ('emp_depart', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='onetoone.Employees')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onetoone.Roles')),
            ],
        ),
    ]
