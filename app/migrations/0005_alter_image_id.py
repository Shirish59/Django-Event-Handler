# Generated by Django 5.0.2 on 2024-02-28 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_image_caption_alter_rimage_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
