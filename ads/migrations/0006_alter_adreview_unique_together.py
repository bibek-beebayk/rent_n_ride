# Generated by Django 4.0 on 2022-03-11 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_rename_recepient_message_receiver_message_email_and_more'),
        ('ads', '0005_adreview_user'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='adreview',
            unique_together={('ad', 'user')},
        ),
    ]
