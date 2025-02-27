# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-08-27 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("django_orghierarchy", "0005_add_fields_to_organization_class"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="organization",
            options={
                "permissions": (
                    ("add_affiliated_organization", "Can add affiliated organization"),
                    (
                        "change_affiliated_organization",
                        "Can change affiliated organization",
                    ),
                    (
                        "delete_affiliated_organization",
                        "Can delete affiliated organization",
                    ),
                    (
                        "replace_organization",
                        "Can replace an organization with a new one",
                    ),
                )
            },
        ),
        migrations.AddField(
            model_name="datasource",
            name="user_editable",
            field=models.BooleanField(
                default=False, verbose_name="Objects may be edited by users"
            ),
        ),
    ]
