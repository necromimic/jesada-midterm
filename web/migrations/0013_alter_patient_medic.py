# Generated by Django 3.2.7 on 2021-09-11 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_patient_medic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='medic',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='web.medic'),
        ),
    ]
