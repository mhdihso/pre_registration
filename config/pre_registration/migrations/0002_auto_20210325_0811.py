# Generated by Django 3.1.7 on 2021-03-25 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pre_registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extraqu',
            name='type_qu',
            field=models.TextField(choices=[('1', 'Multiple options'), ('2', 'Descriptive '), ('3', 'Date')], default='2', max_length=1),
        ),
    ]
