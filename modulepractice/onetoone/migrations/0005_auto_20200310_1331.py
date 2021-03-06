# Generated by Django 2.2.6 on 2020-03-10 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onetoone', '0004_auto_20191222_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('date_created', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('creator', models.CharField(max_length=20)),
                ('paradigm', models.CharField(max_length=20)),
                ('date_created', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Programmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onetoone.Company')),
                ('languages', models.ManyToManyField(to='onetoone.Language')),
            ],
        ),
        migrations.RemoveField(
            model_name='employees',
            name='depart',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='designation',
        ),
        migrations.DeleteModel(
            name='Departments',
        ),
        migrations.DeleteModel(
            name='Employees',
        ),
        migrations.DeleteModel(
            name='Roles',
        ),
    ]
