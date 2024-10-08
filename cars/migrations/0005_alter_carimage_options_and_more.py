# Generated by Django 5.1.1 on 2024-09-26 11:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_carimage_image_number_alter_carimage_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carimage',
            options={'ordering': ['id']},
        ),
        migrations.AlterUniqueTogether(
            name='carimage',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='carimage',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='cars.car'),
        ),
        migrations.RemoveField(
            model_name='carimage',
            name='image_number',
        ),
    ]
