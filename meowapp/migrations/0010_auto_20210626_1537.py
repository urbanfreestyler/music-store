# Generated by Django 3.2 on 2021-06-26 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meowapp', '0009_auto_20210626_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='beat',
            name='key',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='beat',
            name='price',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='beat',
            name='tempo',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.DeleteModel(
            name='Key',
        ),
        migrations.DeleteModel(
            name='Price',
        ),
        migrations.AddField(
            model_name='beat',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='meowapp.genre'),
        ),
    ]