# Generated by Django 2.2.4 on 2019-08-30 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20190830_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]
