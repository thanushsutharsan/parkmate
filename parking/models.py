# database models used by ParkMate.

from datetime import timedelta
from urllib.parse import urlparse

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils import timezone


# allowed official parking sources
OFFICIAL_HOST_SUFFIXES = ("gov.uk", "npp.org.uk")


def validate_official_source(value):
    host = (urlparse(value).hostname or "").lower()

    if not any(
        host == suffix or host.endswith("." + suffix)
        for suffix in OFFICIAL_HOST_SUFFIXES
    ):
        raise ValidationError(
            "ParkMate only accepts official council/GOV.UK or "
            "National Parking Platform source URLs."
        )


class ParkingLocation(models.Model):
    PARKING_TYPES = [
        ("car_park", "Car park"),
        ("multi_storey", "Multi-storey"),
        ("on_street", "On-street parking"),
    ]

    NATIONS = [
        ("england", "England"),
        ("scotland", "Scotland"),
        ("wales", "Wales"),
        ("northern_ireland", "Northern Ireland"),
    ]

    # main parking details
    name = models.CharField(max_length=140)
    address = models.CharField(max_length=220)
    postcode = models.CharField(max_length=10, blank=True)

    nation = models.CharField(
        max_length=24,
        choices=NATIONS,
    )

    local_authority = models.CharField(max_length=160)

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
    )

    parking_type = models.CharField(
        max_length=20,
        choices=PARKING_TYPES,
        default="car_park",
    )

    operator_name = models.CharField(
        max_length=160,
        blank=True,
    )

    spaces_total = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    disabled_spaces = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    # Parking prices and restrictions
    tariff_info = models.TextField(
        blank=True,
        help_text=(
            "Price information. Official records use the "
            "current council/NPP tariff."
        ),
    )

    charging_times = models.CharField(
        max_length=220,
        blank=True,
    )

    restrictions = models.TextField(blank=True)

    payment_info = models.CharField(
        max_length=220,
        blank=True,
    )

    payment_location_code = models.CharField(
        max_length=40,
        blank=True,
    )

    # official source information
    source_name = models.CharField(
        max_length=180,
        blank=True,
    )

    source_url = models.URLField(
        max_length=700,
        blank=True,
        validators=[validate_official_source],
    )

    council_verified = models.BooleanField(default=False)

    last_checked = models.DateTimeField(
        null=True,
        blank=True,
    )

    # optional parking image
    image_url = models.URLField(
        max_length=1000,
        blank=True,
    )

    image_source_url = models.URLField(
        max_length=1000,
        blank=True,
    )

    image_credit = models.CharField(
        max_length=220,
        blank=True,
    )

    # user who added the location
    submitted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="parking_submissions",
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

        indexes = [
            models.Index(
                fields=["nation", "local_authority"],
                name="parking_par_nation_a_idx",
            ),
            models.Index(
                fields=["latitude", "longitude"],
                name="parking_par_latitud_idx",
            ),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            "parking:detail",
            args=[self.pk],
        )

    # checks parking data before saving
    def clean(self):
        super().clean()

        if (
            self.latitude is not None
            and not 49 <= float(self.latitude) <= 61.5
        ):
            raise ValidationError(
                {
                    "latitude": (
                        "Enter a latitude within the United Kingdom."
                    )
                }
            )

        if (
            self.longitude is not None
            and not -8.7 <= float(self.longitude) <= 2
        ):
            raise ValidationError(
                {
                    "longitude": (
                        "Enter a longitude within the United Kingdom."
                    )
                }
            )

        if (
            self.spaces_total is not None
            and self.disabled_spaces is not None
            and self.disabled_spaces > self.spaces_total
        ):
            raise ValidationError(
                {
                    "disabled_spaces": (
                        "Disabled spaces cannot be greater "
                        "than total spaces."
                    )
                }
            )

        if self.council_verified:
            if not self.source_url:
                raise ValidationError(
                    {
                        "source_url": (
                            "A verified location must have "
                            "an official source URL."
                        )
                    }
                )

            if not self.last_checked:
                raise ValidationError(
                    {
                        "last_checked": (
                            "A verified location must have "
                            "a last checked date."
                        )
                    }
                )

            if not self.tariff_info.strip():
                raise ValidationError(
                    {
                        "tariff_info": (
                            "A verified location must include "
                            "the official tariff."
                        )
                    }
                )

    @property
    def is_community_submission(self):
        return not self.council_verified

    @property
    def latest_report(self):
        return self.reports.order_by("-created_at").first()

    @property
    def has_verified_details(self):
        return bool(
            self.council_verified
            and self.source_url
            and self.last_checked
            and self.tariff_info
        )

    @property
    def verification_is_current(self):
        if not self.last_checked:
            return False

        return (
            self.last_checked
            >= timezone.now() - timedelta(days=45)
        )


class AvailabilityReport(models.Model):
    STATUS_CHOICES = [
        ("available", "Spaces available"),
        ("busy", "Busy / nearly full"),
        ("full", "Full"),
    ]

    # parking location being reported
    location = models.ForeignKey(
        ParkingLocation,
        on_delete=models.CASCADE,
        related_name="reports",
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="parking_reports",
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
    )

    spaces_available = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    note = models.CharField(
        max_length=180,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"{self.location} - "
            f"{self.get_status_display()}"
        )


class Favourite(models.Model):
    # saves a parking location to a user's favourites
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="parking_favourites",
    )

    parking = models.ForeignKey(
        ParkingLocation,
        on_delete=models.CASCADE,
        related_name="favourited_by",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

        constraints = [
            models.UniqueConstraint(
                fields=["user", "parking"],
                name="unique_user_parking_favourite",
            ),
        ]

    def __str__(self):
        return f"{self.user} saved {self.parking}"