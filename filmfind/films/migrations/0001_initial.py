# Generated by Django 4.1.4 on 2023-01-02 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('year', models.PositiveIntegerField()),
                ('rating', models.FloatField()),
                ('synopsis', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('year', models.PositiveIntegerField()),
                ('rating', models.FloatField()),
                ('synopsis', models.TextField()),
                ('season_count', models.PositiveIntegerField()),
            ],
        ),
    ]