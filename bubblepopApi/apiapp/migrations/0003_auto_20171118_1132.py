# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 11:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apiapp', '0002_media_political_view'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shown_news', models.IntegerField(default=0, verbose_name='뉴스피드 등장한 뉴스')),
                ('clicked_news', models.IntegerField(default=0, verbose_name='클릭한 뉴스')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='사용자')),
            ],
        ),
        migrations.RemoveField(
            model_name='cachedarticle',
            name='article',
        ),
        migrations.RemoveField(
            model_name='cachedarticle',
            name='cluster',
        ),
        migrations.RemoveField(
            model_name='article',
            name='article_rss',
        ),
        migrations.AddField(
            model_name='article',
            name='cluster',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='apiapp.Cluster', verbose_name='클러스터'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CachedArticle',
        ),
    ]