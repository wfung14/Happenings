# Generated by Django 4.2.2 on 2023-06-21 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_event_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='vendors',
            field=models.ManyToManyField(blank=True, to='main_app.vendor'),
        ),
    ]