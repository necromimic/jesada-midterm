# Generated by Django 3.2.7 on 2021-09-11 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_hospital'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='medic',
        ),
        migrations.DeleteModel(
            name='Hospital',
        ),
        migrations.DeleteModel(
            name='Medic',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
