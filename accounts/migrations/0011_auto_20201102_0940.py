# Generated by Django 3.1.2 on 2020-11-02 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20201102_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pescado',
            name='tamanho',
            field=models.IntegerField(null=True),
        ),
    ]