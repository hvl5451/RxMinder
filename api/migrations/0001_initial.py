# Generated by Django 2.2.5 on 2019-09-08 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PillDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(max_length=250, null=True)),
                ('medicine_name', models.CharField(max_length=250, null=True)),
                ('pill_per_dose', models.CharField(max_length=250, null=True)),
                ('doses_per_day', models.CharField(max_length=250, null=True)),
                ('total_qty', models.CharField(max_length=10, null=True)),
                ('mg_dose', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]