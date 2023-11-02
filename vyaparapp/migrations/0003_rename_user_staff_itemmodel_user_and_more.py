# Generated by Django 4.2.6 on 2023-11-02 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vyaparapp', '0002_itemmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemmodel',
            old_name='user_staff',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='itemmodel',
            name='item_at_price',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
