# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-24 17:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('video_file', models.FileField(max_length=200, upload_to='videos/')),
                ('logo', models.FileField(upload_to='images/')),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ManyToManyField(to='bench.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=50)),
                ('country_code', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_name', models.CharField(max_length=45)),
                ('currency_code', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='CurrencyName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_name', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('platform', models.CharField(max_length=45)),
                ('accepting', models.CharField(max_length=45)),
                ('minimum_investment', models.IntegerField(default=0)),
                ('soft_cap', models.IntegerField(default=0)),
                ('hard_cap', models.IntegerField(default=0)),
                ('bonus', models.CharField(blank=True, max_length=45)),
                ('bounty', models.CharField(blank=True, max_length=45)),
                ('Whitelist_KYC', models.CharField(blank=True, max_length=45)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='bench.Company')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='bench.Country')),
                ('restricted_areas', models.ManyToManyField(to='bench.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ico_profile', models.CharField(max_length=25)),
                ('team', models.CharField(max_length=25)),
                ('vision', models.CharField(max_length=25)),
                ('product', models.CharField(max_length=25)),
                ('total_rating', models.IntegerField(blank=True, default=0)),
                ('company', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='bench.Company')),
            ],
        ),
    ]
