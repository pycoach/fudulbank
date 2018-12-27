# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-17 08:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0079_add_edited_status'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('accounts', '0011_profile_primary_interest'),
    ]

    operations = [
        migrations.RenameField(model_name='profile',
            old_name='primary_interest',
            new_name='main_interest'),
        migrations.CreateModel(
            name='PrimaryInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('object_id', models.PositiveIntegerField(null=True, blank=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exams.Category')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', null=True, blank=True)),
                ('exam', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exams.Exam')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='accounts.PrimaryInterest')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='primary_interest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.PrimaryInterest', limit_choices_to={'children__isnull': True}),
        ),
    ]
