# Generated by Django 2.2.6 on 2019-12-22 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_auto_20191222_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department_name',
            field=models.ManyToManyField(null=True, to='departments.Department'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='role_name',
            field=models.ManyToManyField(null=True, to='roles.Role'),
        ),
    ]