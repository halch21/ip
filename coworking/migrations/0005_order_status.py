# Generated by Django 3.1.5 on 2021-04-08 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coworking', '0004_auto_20210408_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(0, 'Не оплачен'), (1, 'Оплачен')], default=0),
        ),
    ]
