# Generated by Django 4.0 on 2022-03-14 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_rename_recepient_message_receiver_message_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='province',
            field=models.CharField(choices=[('Province 1', 'Province 1'), ('Madhesh', 'Madhesh'), ('Bagmati', 'Bagmati'), ('Gandaki', 'Gandaki'), ('Lumbini', 'Lumbini'), ('Karnali', 'Karnali'), ('Sudurpaschim', 'Sudurpaschim')], max_length=20, null=True),
        ),
    ]
