# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-29 12:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formdata',
            options={'verbose_name_plural': 'Form data'},
        ),
        migrations.RenameField(
            model_name='formdata',
            old_name='form_data',
            new_name='form_field',
        ),
    ]