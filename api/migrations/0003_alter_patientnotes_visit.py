# Generated by Django 4.1.3 on 2022-11-15 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_patient_bloodtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientnotes',
            name='visit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.patientvisit'),
        ),
    ]