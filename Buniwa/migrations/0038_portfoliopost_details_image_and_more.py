# Generated by Django 5.0.6 on 2024-05-24 12:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buniwa', '0037_alter_portfoliopost_options_portfoliopost_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliopost',
            name='details_image',
            field=models.ImageField(default=datetime.datetime(2024, 5, 24, 12, 7, 17, 695770, tzinfo=datetime.timezone.utc), upload_to='card_images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfoliopost',
            name='portfolio_details_description',
            field=models.TextField(default=datetime.datetime(2024, 5, 24, 12, 7, 52, 593456, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='portfoliopost',
            name='description',
            field=models.CharField(max_length=80),
        ),
    ]