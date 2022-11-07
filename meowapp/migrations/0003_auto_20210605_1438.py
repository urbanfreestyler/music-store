# Generated by Django 3.2 on 2021-06-05 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meowapp', '0002_rename_customer_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beat',
            old_name='length',
            new_name='duration',
        ),
        migrations.RemoveField(
            model_name='order',
            name='email',
        ),
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='beat',
            field=models.ForeignKey(default=None, max_length=100, on_delete=django.db.models.deletion.CASCADE, to='meowapp.beat'),
        ),
    ]
