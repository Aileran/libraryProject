# Generated by Django 3.2.9 on 2021-12-07 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('artist', models.CharField(blank=True, max_length=60)),
                ('label', models.CharField(blank=True, max_length=60)),
                ('genre', models.CharField(blank=True, max_length=60)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('comment', models.TextField(blank=True)),
                ('owner', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('author', models.CharField(blank=True, max_length=60)),
                ('publisher', models.CharField(blank=True, max_length=60)),
                ('genre', models.CharField(blank=True, max_length=60)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('comment', models.TextField(blank=True)),
                ('owner', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('director', models.CharField(blank=True, max_length=60)),
                ('studio', models.CharField(blank=True, max_length=60)),
                ('genre', models.CharField(blank=True, max_length=60)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('comment', models.TextField(blank=True)),
                ('owner', models.CharField(blank=True, max_length=150)),
            ],
        ),
    ]
