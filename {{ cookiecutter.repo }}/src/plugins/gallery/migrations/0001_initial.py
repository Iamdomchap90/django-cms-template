# Generated by Django 4.2.2 on 2023-06-13 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ("cms", "0022_auto_20180620_1551"),
    ]

    operations = [
        migrations.CreateModel(
            name="GalleryBlock",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="%(app_label)s_%(class)s",
                        serialize=False,
                        to="cms.cmsplugin",
                    ),
                ),
                (
                    "display",
                    models.CharField(
                        choices=[("carousel", "Carousel"), ("thumbnails", "Thumbnails")],
                        default="carousel",
                        max_length=255,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("cms.cmsplugin",),
        ),
        migrations.CreateModel(
            name="GalleryImage",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="%(app_label)s_%(class)s",
                        serialize=False,
                        to="cms.cmsplugin",
                    ),
                ),
                (
                    "photo_credit",
                    models.CharField(
                        blank=True,
                        help_text="This will only be displayed on the modal",
                        max_length=255,
                    ),
                ),
                (
                    "image",
                    filer.fields.image.FilerImageField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.FILER_IMAGE_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("cms.cmsplugin",),
        ),
    ]
