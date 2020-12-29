# Generated by Django 3.1.3 on 2020-11-14 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('f_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('age', models.PositiveIntegerField(verbose_name='Age')),
                ('bday', models.DateField()),
                ('contact', models.CharField(max_length=100, verbose_name='Contact No.')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('drug_name', models.CharField(max_length=100, verbose_name='Drug Name')),
                ('dosage', models.IntegerField(verbose_name='Dosage')),
                ('route', models.CharField(max_length=100, verbose_name='Route Taken')),
                ('frequency', models.CharField(max_length=255, verbose_name='Frequency')),
                ('amount_dispensed', models.IntegerField(verbose_name='Amount Dispensed')),
                ('no_of_refills', models.IntegerField(verbose_name='No of Refills')),
                ('expiration_date', models.DateField()),
                ('active', models.BooleanField(default=False)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prescribe_app.patientinformation', verbose_name='Patient')),
            ],
            options={
                'db_table': 'prescription',
            },
        ),
    ]
