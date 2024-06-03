# Generated by Django 3.2.24 on 2024-04-09 14:57

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0058_remove_tr_tr_collation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="translation",
            name="machinery_sources",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    choices=[
                        ("translation-memory", "Translation Memory"),
                        ("concordance-search", "Concordance Search"),
                        ("google-translate", "Google Translate"),
                        ("microsoft-translator", "Microsoft Translator"),
                        ("systran-translate", "Systran Translate"),
                        ("microsoft-terminology", "Microsoft"),
                        ("caighdean", "Caighdean"),
                        ("gpt-transform", "GPT Transform"),
                    ],
                    max_length=30,
                ),
                blank=True,
                default=list,
                size=None,
            ),
        ),
    ]