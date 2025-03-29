# Generated by Django 5.1.7 on 2025-03-29 11:55

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('category', models.CharField(choices=[('APP', 'Appetizer'), ('MAIN', 'Main Course'), ('DESS', 'Dessert'), ('BEV', 'Beverage')], max_length=4)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default="ALI'S FOOD", max_length=100)),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('max_capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('number_of_guests', models.IntegerField()),
                ('special_requests', models.TextField(blank=True)),
                ('is_cancelled', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('special_instructions', models.TextField(blank=True)),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.menu')),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.reservation')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.CharField(max_length=10)),
                ('capacity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.restaurant')),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.table'),
        ),
    ]
