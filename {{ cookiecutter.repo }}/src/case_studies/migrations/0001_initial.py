# Generated by Django 4.2.13 on 2024-07-08 08:35

import cms.models.fields
import core.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import filer.fields.image
import giant_search.mixins
import taggit_autosuggest.managers


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ("cms", "0022_auto_20180620_1551"),
        ("taggit", "0005_auto_20220424_2025"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_at", core.fields.AutoDateTimeField(default=django.utils.timezone.now)),
                ("name", models.CharField(max_length=255)),
                ("slug", models.SlugField(unique=True)),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="CaseStudy",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("meta_title", models.CharField(blank=True, max_length=255)),
                ("meta_description", models.CharField(blank=True, max_length=255)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_at", core.fields.AutoDateTimeField(default=django.utils.timezone.now)),
                (
                    "is_published",
                    models.BooleanField(
                        default=False, help_text="Selecting this option will publish this item"
                    ),
                ),
                (
                    "publish_at",
                    models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
                ),
                ("title", models.CharField(max_length=255)),
                ("slug", models.SlugField(max_length=255, unique=True)),
                ("description", models.TextField()),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="case_studies.category",
                    ),
                ),
                (
                    "content",
                    cms.models.fields.PlaceholderField(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        slotname="case_study_content",
                        to="cms.placeholder",
                    ),
                ),
                (
                    "image",
                    filer.fields.image.FilerImageField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.FILER_IMAGE_MODEL,
                    ),
                ),
                (
                    "tags",
                    taggit_autosuggest.managers.TaggableManager(
                        help_text="A comma-separated list of tags.",
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="Tags",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Case Studies",
            },
            bases=(giant_search.mixins.SearchableMixin, models.Model),
        ),
    ]
