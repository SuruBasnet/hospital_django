# Generated by Django 4.1.3 on 2022-11-16 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_defaultbillingledger_patientstatus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sampletypetest',
            name='sampleId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.sample'),
        ),
    ]
