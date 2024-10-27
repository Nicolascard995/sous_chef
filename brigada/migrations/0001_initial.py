# Generated by Django 5.1.2 on 2024-10-27 13:05

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
            name='InventoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit', models.CharField(choices=[('kg', 'Kilogramo'), ('g', 'Gramo'), ('litro', 'Litro'), ('ml', 'Mililitro')], max_length=50)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ingredients', models.TextField()),
                ('steps', models.TextField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Chef', 'Chef'), ('Sous Chef', 'Sous Chef'), ('Cocinero', 'Cocinero')], max_length=50)),
                ('schedule', models.CharField(choices=[('Lunes a Viernes, 9am-5pm', 'Lunes a Viernes, 9am-5pm'), ('Lunes a Viernes, 2pm-10pm', 'Lunes a Viernes, 2pm-10pm'), ('Sábados y Domingos, 10am-6pm', 'Sábados y Domingos, 10am-6pm')], max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
