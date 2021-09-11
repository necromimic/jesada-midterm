# Generated by Django 3.2.7 on 2021-09-11 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_delete_hospital'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hosname', models.CharField(max_length=50, verbose_name='ชื่อโรงพยาบาล')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='web.patient')),
            ],
            options={
                'verbose_name': 'Hospital',
                'verbose_name_plural': 'Hospitals',
            },
        ),
    ]