# Generated by Django 5.0.1 on 2024-01-02 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_year', models.CharField(blank=True, max_length=50)),
                ('intensity', models.IntegerField()),
                ('sector', models.CharField(max_length=100)),
                ('topic', models.CharField(max_length=100)),
                ('insight', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('region', models.CharField(max_length=100)),
                ('start_year', models.CharField(blank=True, max_length=50)),
                ('impact', models.CharField(blank=True, max_length=100)),
                ('added', models.CharField(max_length=50)),
                ('published', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=100)),
                ('relevance', models.IntegerField()),
                ('pestle', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('title', models.TextField()),
                ('likelihood', models.IntegerField()),
            ],
        ),
    ]
