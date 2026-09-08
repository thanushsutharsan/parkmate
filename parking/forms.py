# forms used for parking and user input.

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import AvailabilityReport, ParkingLocation


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]

    # checks if the email is already used
    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()

        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                "An account with this email address already exists."
            )

        return email


class AvailabilityReportForm(forms.ModelForm):
    class Meta:
        model = AvailabilityReport
        fields = [
            "status",
            "spaces_available",
            "note",
        ]

        widgets = {
            "note": forms.TextInput(),
        }

    def __init__(self, *args, location=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.location = location

    # checks the reported space amount
    def clean(self):
        cleaned_data = super().clean()

        status = cleaned_data.get("status")
        spaces_available = cleaned_data.get("spaces_available")

        if status == "full" and spaces_available not in (None, 0):
            self.add_error(
                "spaces_available",
                "A full car park cannot have available spaces.",
            )

        if (
            self.location
            and self.location.spaces_total is not None
            and spaces_available is not None
            and spaces_available > self.location.spaces_total
        ):
            self.add_error(
                "spaces_available",
                "Available spaces cannot be greater than the "
                "car park capacity.",
            )

        return cleaned_data


class CommunityParkingLocationForm(forms.ModelForm):
    # form used for community parking submissions
    class Meta:
        model = ParkingLocation

        fields = [
            "name",
            "address",
            "postcode",
            "nation",
            "local_authority",
            "latitude",
            "longitude",
            "parking_type",
            "operator_name",
            "spaces_total",
            "disabled_spaces",
            "tariff_info",
            "charging_times",
            "restrictions",
            "payment_info",
        ]

        labels = {
            "local_authority": "Town / local authority",
            "operator_name": "Operator (if known)",
            "tariff_info": "Price information (if known)",
        }

        help_texts = {
            "latitude": (
                "Use the parking location's latitude, "
                "for example 51.389000."
            ),
            "longitude": (
                "Use the parking location's longitude, "
                "for example 0.548000."
            ),
            "tariff_info": (
                "Community-submitted prices are never labelled "
                "Council/NPP verified."
            ),
        }

        widgets = {
            "address": forms.TextInput(),
            "postcode": forms.TextInput(),
            "latitude": forms.NumberInput(
                attrs={"step": "0.000001"}
            ),
            "longitude": forms.NumberInput(
                attrs={"step": "0.000001"}
            ),
            "tariff_info": forms.Textarea(
                attrs={"rows": 2}
            ),
            "restrictions": forms.Textarea(
                attrs={"rows": 3}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["operator_name"].required = False
        self.fields["tariff_info"].required = False

        # adds the same css class to each field
        for field in self.fields.values():
            field.widget.attrs.setdefault(
                "class",
                "form-control",
            )

    # formats the postcode
    def clean_postcode(self):
        return (
            self.cleaned_data
            .get("postcode", "")
            .strip()
            .upper()
        )


class ParkingLocationForm(forms.ModelForm):
    # form used for official parking records
    class Meta:
        model = ParkingLocation

        fields = [
            "name",
            "address",
            "postcode",
            "nation",
            "local_authority",
            "latitude",
            "longitude",
            "parking_type",
            "operator_name",
            "spaces_total",
            "disabled_spaces",
            "tariff_info",
            "charging_times",
            "restrictions",
            "payment_info",
            "payment_location_code",
            "source_name",
            "source_url",
            "last_checked",
            "image_url",
            "image_source_url",
            "image_credit",
            "is_active",
        ]

        widgets = {
            "address": forms.TextInput(),
            "postcode": forms.TextInput(),
            "latitude": forms.NumberInput(
                attrs={"step": "0.000001"}
            ),
            "longitude": forms.NumberInput(
                attrs={"step": "0.000001"}
            ),
            "tariff_info": forms.Textarea(
                attrs={"rows": 3}
            ),
            "restrictions": forms.Textarea(
                attrs={"rows": 3}
            ),
            "last_checked": forms.DateTimeInput(
                attrs={"type": "datetime-local"},
                format="%Y-%m-%dT%H:%M",
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["last_checked"].input_formats = [
            "%Y-%m-%dT%H:%M"
        ]

        self.fields["operator_name"].required = True
        self.fields["source_name"].required = True
        self.fields["source_url"].required = True
        self.fields["tariff_info"].required = True

        # adds the same css class to each field
        for field in self.fields.values():
            field.widget.attrs.setdefault(
                "class",
                "form-control",
            )