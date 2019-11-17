# Generated by Django 2.2.7 on 2019-11-14 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerRun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('distance', models.DecimalField(decimal_places=2, max_digits=99)),
                ('time', models.DecimalField(decimal_places=2, max_digits=99)),
            ],
        ),
    ]
