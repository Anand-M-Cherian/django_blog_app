# Generated by Django 5.1.3 on 2024-11-10 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='banner',
            field=models.ImageField(blank=True, default='fallback.jpg', upload_to=''),
        ),
    ]
