# Generated by Django 4.1 on 2022-09-04 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_cuenta_celular'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='nacimiento',
            #
            field=models.DateField(default='2022-01-01'),
            preserve_default=False,
        ),
    ]
