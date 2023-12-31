# Generated by Django 3.2.23 on 2023-12-08 19:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserInfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('work_address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=30)),
                ('zip', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Zip code must be in the format XXXXX or XXXXX-XXXX', regex='^\\d{5}(?:-\\d{4})?$')])),
                ('phone', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Phone number must be in the format XXX-XXX-XXXX', regex='^\\d{3}-\\d{3}-\\d{4}$')])),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserInfo.userinformation')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=100)),
                ('school_state', models.CharField(max_length=100)),
                ('school_city', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('school_start_date', models.DateField()),
                ('school_end_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserInfo.userinformation')),
            ],
        ),
    ]
