# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-02 11:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btitle', models.CharField(max_length=10, verbose_name='书名')),
                ('bpub_date', models.DateField(verbose_name='发布日期')),
                ('bread', models.IntegerField(default=0)),
                ('bcomment', models.IntegerField(default=0)),
                ('is_delete', models.BooleanField(default=False)),
                ('is_d', models.IntegerField(default=0)),
                ('image', models.ImageField(null=True, upload_to='bookset', verbose_name='图片')),
            ],
            options={
                'verbose_name': '图书',
                'verbose_name_plural': '图书',
                'db_table': 'tb_books',
            },
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=20)),
                ('hgender', models.SmallIntegerField(choices=[(0, '女'), (1, '男')], default=0)),
                ('hcomment', models.CharField(max_length=200, null=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('hbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='heros', to='setbook.BookInfo')),
            ],
            options={
                'verbose_name': '英雄',
                'verbose_name_plural': '英雄',
                'db_table': 'tb_heros',
            },
        ),
    ]
