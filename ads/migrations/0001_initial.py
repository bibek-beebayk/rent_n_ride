# Generated by Django 4.0 on 2021-12-22 03:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('available_from', models.DateField(null=True)),
                ('available_till', models.DateField(null=True)),
                ('asking_price', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('featured_image', models.ImageField(blank=True, default='ads/ad-default.jpg', null=True, upload_to='ads/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
