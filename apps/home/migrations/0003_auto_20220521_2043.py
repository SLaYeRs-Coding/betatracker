# Generated by Django 3.2.6 on 2022-05-21 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_application_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='size_type',
            field=models.CharField(default=0, max_length=225),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='application',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
