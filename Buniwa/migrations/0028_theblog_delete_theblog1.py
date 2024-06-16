# Generated by Django 5.0.6 on 2024-05-21 19:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buniwa', '0027_theblog1_delete_theblog_alter_blog_category_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='theBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('published_date', models.DateField()),
                ('blog_image', models.ImageField(upload_to='card_images/')),
                ('author_image', models.ImageField(upload_to='author_images/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Blogs Section',
            },
        ),
        migrations.DeleteModel(
            name='theBlog1',
        ),
    ]