# Generated by Django 2.2.5 on 2021-07-24 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0008_auto_20210718_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to='room_photos'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='rooms.Room'),
        ),
    ]
