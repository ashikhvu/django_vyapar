# Generated by Django 4.2.6 on 2023-11-03 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vyaparapp', '0006_transactionmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionmodel',
            name='trans_invoice',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
    ]
