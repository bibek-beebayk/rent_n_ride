# Generated by Django 4.0 on 2021-12-23 02:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleMake',
            fields=[
                ('make', models.CharField(max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='vehicle',
            name='make',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='vehicles.vehiclemake'),
        ),
    ]