# Generated by Django 3.1.5 on 2021-04-07 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coworking', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='manager',
            field=models.CharField(default=1111, max_length=100),
            preserve_default=False,
        ),
    ]
