# Generated by Django 3.2.9 on 2022-03-31 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_auto_20220331_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocks',
            name='AVG_PRICE',
            field=models.FloatField(default=56),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stocks',
            name='DELIV_PER',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stocks',
            name='DELIV_QTY',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
    ]
