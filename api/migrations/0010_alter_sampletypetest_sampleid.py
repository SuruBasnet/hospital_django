# Generated by Django 4.1.3 on 2022-11-21 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_sampletypetest_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sampletypetest',
            name='sampleId',
            field=models.IntegerField(null=True),
        ),
    ]
