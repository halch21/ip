# Generated by Django 3.1.5 on 2021-04-07 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('days', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeRooom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('number', models.CharField(max_length=10)),
                ('customer', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('period', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='coworking.period')),
                ('type_room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='coworking.typerooom')),
            ],
        ),
    ]
