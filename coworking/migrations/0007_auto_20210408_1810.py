# Generated by Django 3.1.5 on 2021-04-08 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coworking', '0006_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='coworking.staff'),
        ),
    ]
