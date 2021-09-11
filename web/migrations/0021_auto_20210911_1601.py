# Generated by Django 3.2.7 on 2021-09-11 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0020_hospital'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='patient',
        ),
        migrations.AddField(
            model_name='medic',
            name='affiliation',
            field=models.ManyToManyField(default=None, to='web.Hospital'),
        ),
        migrations.AddField(
            model_name='patient',
            name='hospital',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='web.hospital'),
        ),
    ]
