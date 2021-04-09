# Generated by Django 3.1.5 on 2021-04-08 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coworking', '0005_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('post', models.IntegerField(choices=[(3, 'Младший менеджер'), (2, 'Менеджер'), (1, 'Старший менеджер')])),
            ],
        ),
    ]
