# Generated by Django 5.1.3 on 2025-01-22 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReadEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('fiction', 'Fiction'), ('nonfiction', 'Non-fiction'), ('science', 'Science'), ('history', 'History'), ('fantasy', 'Fantasy'), ('biography', 'Biography')], max_length=20)),
                ('status', models.CharField(choices=[('incomplted', 'incompleted'), ('inprogress', 'inprogress'), ('complted', 'completed')], max_length=30)),
                ('total_pages', models.PositiveIntegerField()),
                ('pages_read', models.PositiveIntegerField(default=0)),
                ('progress', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(null=True, upload_to='book_images/')),
            ],
        ),
    ]
