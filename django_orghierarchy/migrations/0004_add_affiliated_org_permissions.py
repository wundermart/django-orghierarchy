# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-15 09:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("django_orghierarchy", "0003_rm_responsible_org_add_internal_type"),
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
                )
            },
        ),
    ]
