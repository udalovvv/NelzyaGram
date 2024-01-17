# Generated by Django 4.1.4 on 2024-01-17 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to='photo')),
                ('about_user', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_of_publication', models.TextField(max_length=1000)),
                ('image_of_publication', models.ImageField(upload_to='images')),
                ('owner_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publication_set', to='Profile.user')),
            ],
        ),
    ]
