# sets up parkmate models in django admin.

from django.contrib import admin
from django.utils import timezone

from .models import AvailabilityReport, Favourite, ParkingLocation


# marks selected locations as checked
@admin.action(description="Mark selected official details as checked now")
def mark_checked_now(modeladmin, request, queryset):
    queryset.update(last_checked=timezone.now())


@admin.register(ParkingLocation)
class ParkingLocationAdmin(admin.ModelAdmin):
    # columns shown in the admin list
    list_display = (
        "name",
        "local_authority",
        "nation",
        "council_verified",
        "submitted_by",
        "spaces_total",
        "last_checked",
        "is_active",
    )

    # filters shown in the admin
    list_filter = (
        "council_verified",
        "nation",
        "parking_type",
        "is_active",
        "local_authority",
    )

    # fields that can be searched
    search_fields = (
        "name",
        "address",
        "postcode",
        "local_authority",
        "source_name",
        "submitted_by__username",
    )

    actions = [mark_checked_now]

    # groups fields in the edit page
    fieldsets = (
        (
            "Location",
            {
                "fields": (
                    "name",
                    "address",
                    "postcode",
                    "nation",
                    "local_authority",
                    "latitude",
                    "longitude",
                    "parking_type",
                )
            },
        ),
        (
            "Parking details",
            {
                "fields": (
                    "operator_name",
                    "spaces_total",
                    "disabled_spaces",
                    "tariff_info",
                    "charging_times",
                    "restrictions",
                    "payment_info",
                    "payment_location_code",
                )
            },
        ),
        (
            "Verification",
            {
                "fields": (
                    "source_name",
                    "source_url",
                    "council_verified",
                    "last_checked",
                )
            },
        ),
        (
            "Contribution",
            {
                "fields": (
                    "submitted_by",
                )
            },
        ),
        (
            "Exact-location image",
            {
                "fields": (
                    "image_url",
                    "image_source_url",
                    "image_credit",
                )
            },
        ),
        (
            "Status",
            {
                "fields": (
                    "is_active",
                )
            },
        ),
    )


@admin.register(AvailabilityReport)
class AvailabilityReportAdmin(admin.ModelAdmin):
    # shows parking reports in the admin
    list_display = (
        "location",
        "user",
        "status",
        "spaces_available",
        "created_at",
    )

    list_filter = (
        "status",
        "created_at",
    )

    search_fields = (
        "location__name",
        "user__username",
        "note",
    )


@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    # shows saved parking locations
    list_display = (
        "user",
        "parking",
        "created_at",
    )

    search_fields = (
        "user__username",
        "parking__name",

    )
