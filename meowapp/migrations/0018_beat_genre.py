# Generated by Django 3.2 on 2021-06-28 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meowapp', '0017_auto_20210626_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='beat',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='meowapp.genre'),
        ),
    ]