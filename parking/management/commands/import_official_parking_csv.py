# Imports official parking data from a CSV file.
import csv
from datetime import datetime
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from parking.models import ParkingLocation

REQUIRED = {
    "name",
    "address",
    "postcode",
    "nation",
    "local_authority",
    "latitude",
    "longitude",
    "operator_name",
    "spaces_total",
    "tariff_info",
    "source_name",
    "source_url",
    "last_checked",
}


class Command(BaseCommand):
    help = (
        "Import an official council/NPP parking CSV. "
        "Unofficial source URLs are rejected."
    )

    def add_arguments(self, parser):
        parser.add_argument("csv_path")

    def handle(self, *args, **options):
        path = Path(options["csv_path"])

        if not path.exists():
            raise CommandError(
                f"File not found: {path}"
            )

        with path.open(
            newline="",
            encoding="utf-8-sig",
        ) as handle:
            reader = csv.DictReader(handle)

            missing = REQUIRED - set(
                reader.fieldnames or []
            )

            if missing:
                raise CommandError(
                    "Missing CSV columns: "
                    + ", ".join(
                        sorted(missing)
                    )
                )

            count = 0

            for row_no, row in enumerate(
                reader,
                start=2,
            ):
                try:
                    checked = datetime.fromisoformat(
                        row["last_checked"]
                    )

                    if timezone.is_naive(
                        checked
                    ):
                        checked = (
                            timezone.make_aware(
                                checked
                            )
                        )

                    defaults = {
                        "address": row["address"],
                        "nation": row["nation"],
                        "local_authority": (
                            row[
                                "local_authority"
                            ]
                        ),
                        "latitude": row[
                            "latitude"
                        ],
                        "longitude": row[
                            "longitude"
                        ],
                        "parking_type": (
                            row.get(
                                "parking_type"
                            )
                            or "car_park"
                        ),
                        "operator_name": row[
                            "operator_name"
                        ],
                        "spaces_total": (
                            int(
                                row[
                                    "spaces_total"
                                ]
                            )
                            if row.get(
                                "spaces_total"
                            )
                            else None
                        ),
                        "disabled_spaces": (
                            int(
                                row[
                                    "disabled_spaces"
                                ]
                            )
                            if row.get(
                                "disabled_spaces"
                            )
                            else None
                        ),
                        "tariff_info": row[
                            "tariff_info"
                        ],
                        "charging_times": (
                            row.get(
                                "charging_times",
                                "",
                            )
                        ),
                        "restrictions": (
                            row.get(
                                "restrictions",
                                "",
                            )
                        ),
                        "payment_info": (
                            row.get(
                                "payment_info",
                                "",
                            )
                        ),
                        "payment_location_code": (
                            row.get(
                                "payment_location_code",
                                "",
                            )
                        ),
                        "source_name": row[
                            "source_name"
                        ],
                        "source_url": row[
                            "source_url"
                        ],
                        "last_checked": checked,
                        "council_verified": True,
                        "is_active": True,
                    }

                    obj, _ = (
                        ParkingLocation.objects.update_or_create(
                            name=row["name"],
                            postcode=row[
                                "postcode"
                            ],
                            defaults=defaults,
                        )
                    )

                    obj.full_clean()
                    obj.save()

                    count += 1

                except Exception as exc:
                    raise CommandError(
                        (
                            f"Row {row_no} "
                            "could not be imported: "
                            f"{exc}"
                        )
                    ) from exc

        self.stdout.write(
            self.style.SUCCESS(
                (
                    f"Imported {count} "
                    "verified parking locations."
                )
            )
        )
