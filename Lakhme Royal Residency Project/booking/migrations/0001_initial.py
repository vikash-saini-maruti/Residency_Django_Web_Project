# Generated by Django 4.2.5 on 2023-10-31 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('check_in', models.DateField()),
                ('room_type', models.CharField(choices=[('standard', 'Standard Room'), ('deluxe', 'Deluxe Room'), ('suite', 'Suite')], max_length=10)),
            ],
        ),
    ]
