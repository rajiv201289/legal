# Generated by Django 5.1.5 on 2025-01-29 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legal', '0013_alter_caseentry_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CaseDetails',
        ),
        migrations.DeleteModel(
            name='CaseEntry',
        ),
    ]
