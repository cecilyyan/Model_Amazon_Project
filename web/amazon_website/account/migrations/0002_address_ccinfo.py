# Generated by Django 2.0.1 on 2018-04-20 17:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(default='User address!', max_length=2000)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='CCInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_on_card', models.CharField(default='YOUR NAME', max_length=50)),
                ('cc_no', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 16', regex='^.{16}$')])),
                ('month', models.CharField(choices=[('1', 'January'), ('2', 'February'), ('3', 'March'), ('4', 'April'), ('5', 'May'), ('6', 'June'), ('7', 'July'), ('8', 'August'), ('9', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')], default='1', max_length=16)),
                ('year', models.IntegerField(default=2019, validators=[django.core.validators.MaxValueValidator(2026), django.core.validators.MinValueValidator(2018)])),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Profile')),
            ],
        ),
    ]
