# Generated by Django 4.2.16 on 2024-10-17 17:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0066_userprofile_community_builder_level_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="community_builder_level",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="review_master_level",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="translation_champion_level",
        ),
    ]