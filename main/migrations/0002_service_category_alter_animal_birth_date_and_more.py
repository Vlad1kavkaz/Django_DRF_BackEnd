# Generated by Django 4.2.6 on 2023-10-22 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='category',
            field=models.CharField(default='medecine', max_length=100),
        ),
        migrations.AlterField(
            model_name='animal',
            name='birth_date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
