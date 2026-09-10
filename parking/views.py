# handles the main parkmate page requests.

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import (
    CommunityParkingLocationForm,
    ParkingLocationForm,
    RegisterForm,
)
from .models import Favourite, ParkingLocation


# postcode areas used for search
POSTCODE_SEARCH_AREAS = {
    "B": "Birmingham",
    "CV": "Coventry",
    "DE": "Derby",
    "DY": "Dudley",
    "LE": "Leicester",
    "NG": "Nottingham",
    "ST": "Stoke-on-Trent",
    "WS": "Walsall",
    "WV": "Wolverhampton",
    "M": "Manchester",
    "L": "Liverpool",
    "PR": "Preston",
    "WA": "Warrington",
    "WN": "Wigan",
    "BL": "Bolton",
    "OL": "Oldham",
    "BB": "Blackburn",
    "FY": "Blackpool",
    "LS": "Leeds",
    "BD": "Bradford",
    "HD": "Huddersfield",
    "HX": "Halifax",
    "S": "Sheffield",
    "YO": "York",
    "HU": "Hull",
    "NE": "Newcastle",
    "SR": "Sunderland",
    "DH": "Durham",
    "DL": "Darlington",
    "TS": "Middlesbrough",
    "CA": "Carlisle",
    "LA": "Lancaster",
    "CH": "Chester",
    "CW": "Crewe",
    "TF": "Telford",
    "WR": "Worcester",
    "HR": "Hereford",
    "GL": "Gloucester",
    "BS": "Bristol",
    "BA": "Bath",
    "EX": "Exeter",
    "PL": "Plymouth",
    "TQ": "Torquay",
    "TR": "Truro",
    "TA": "Taunton",
    "BH": "Bournemouth",
    "SO": "Southampton",
    "PO": "Portsmouth",
    "RG": "Reading",
    "OX": "Oxford",
    "MK": "Milton Keynes",
    "LU": "Luton",
    "CB": "Cambridge",
    "IP": "Ipswich",
    "NR": "Norwich",
    "PE": "Peterborough",
    "NN": "Northampton",
    "ME": "Medway",
    "DA": "Dartford",
    "CT": "Canterbury",
    "TN": "Tunbridge Wells",
    "BN": "Brighton",
    "RH": "Crawley",
    "CR": "Croydon",
    "BR": "Bromley",
    "UB": "Southall",
    "CF": "Cardiff",
    "SA": "Swansea",
    "NP": "Newport",
    "LL": "North Wales",
    "SY": "Shrewsbury",
    "EH": "Edinburgh",
    "G": "Glasgow",
    "AB": "Aberdeen",
    "DD": "Dundee",
    "FK": "Falkirk",
    "KY": "Kirkcaldy",
    "PA": "Paisley",
    "PH": "Perth",
    "IV": "Inverness",
    "BT": "Belfast",
}


# gets an area from a postcode search
def postcode_area_query(value):
    compact = "".join(value.upper().split())
    letters = "".join(ch for ch in compact if ch.isalpha())

    # avoids treating normal words as postcodes
    if not any(ch.isdigit() for ch in compact) and len(compact) > 2:
        return ""

    for size in (2, 1):
        prefix = letters[:size]

        if prefix in POSTCODE_SEARCH_AREAS:
            return POSTCODE_SEARCH_AREAS[prefix]

    return ""


# returns active parking locations
def active_locations():
    return ParkingLocation.objects.filter(is_active=True)


def home(request):
    return render(request, "parking/home.html")


def health_check(request):
    return JsonResponse({"status": "ok"})


# shows and filters parking locations
def parking_list(request):
    q = request.GET.get("q", "").strip()
    nation = request.GET.get("nation", "").strip()

    locations = active_locations()

    if q:
        area = postcode_area_query(q)

        query = (
            Q(name__icontains=q)
            | Q(address__icontains=q)
            | Q(postcode__icontains=q)
            | Q(local_authority__icontains=q)
        )

        if area:
            query |= (
                Q(name__icontains=area)
                | Q(address__icontains=area)
                | Q(local_authority__icontains=area)
            )

        locations = locations.filter(query)

    if nation:
        locations = locations.filter(nation=nation)

    favourite_ids = set()

    if request.user.is_authenticated:
        favourite_ids = set(
            Favourite.objects.filter(
                user=request.user
            ).values_list(
                "parking_id",
                flat=True,
            )
        )

    return render(
        request,
        "parking/list.html",
        {
            "locations": locations,
            "q": q,
            "nation": nation,
            "nations": ParkingLocation.NATIONS,
            "favourite_ids": favourite_ids,
        },
    )


# sends parking locations to the map
def map_view(request):
    locations = active_locations().order_by("name")
    q = request.GET.get("q", "").strip()

    if q:
        area = postcode_area_query(q)

        query = (
            Q(name__icontains=q)
            | Q(address__icontains=q)
            | Q(postcode__icontains=q)
            | Q(local_authority__icontains=q)
        )

        if area:
            query |= (
                Q(name__icontains=area)
                | Q(address__icontains=area)
                | Q(local_authority__icontains=area)
            )

        locations = locations.filter(query)

    map_locations = [
        {
            "id": item.id,
            "name": item.name,
            "address": item.address,
            "postcode": item.postcode,
            "price": item.tariff_info or "Price not supplied",
            "lat": float(item.latitude),
            "lon": float(item.longitude),
            "verified": item.council_verified,
        }
        for item in locations
    ]

    return render(
        request,
        "parking/map.html",
        {
            "map_locations": map_locations,
            "q": q,
        },
    )


# shows one parking location
def parking_detail(request, pk):
    location = get_object_or_404(
        active_locations(),
        pk=pk,
    )

    is_favourite = False

    if request.user.is_authenticated:
        is_favourite = Favourite.objects.filter(
            user=request.user,
            parking=location,
        ).exists()

    can_manage = request.user.is_authenticated and (
        request.user.is_staff
        or location.submitted_by_id == request.user.id
    )

    return render(
        request,
        "parking/detail.html",
        {
            "location": location,
            "is_favourite": is_favourite,
            "can_manage": can_manage,
        },
    )


# registers a new user
def register(request):
    if request.user.is_authenticated:
        return redirect("parking:dashboard")

    form = RegisterForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.save()

        login(request, user)

        messages.success(
            request,
            "Account created successfully.",
        )

        return redirect("parking:dashboard")

    return render(
        request,
        "registration/register.html",
        {
            "form": form,
        },
    )


@login_required
# shows saved parking and submissions
def dashboard(request):
    favourites = Favourite.objects.filter(
        user=request.user,
        parking__is_active=True,
    ).select_related("parking")

    submissions = (
        request.user.parking_submissions
        .filter(is_active=True)
        .order_by("-created_at")
    )

    return render(
        request,
        "parking/dashboard.html",
        {
            "favourites": favourites,
            "submissions": submissions,
        },
    )


@login_required
# adds or removes a favourite
def toggle_favourite(request, pk):
    location = get_object_or_404(
        active_locations(),
        pk=pk,
    )

    if request.method == "POST":
        favourite, created = Favourite.objects.get_or_create(
            user=request.user,
            parking=location,
        )

        if created:
            messages.success(
                request,
                f"Saved {location.name}.",
            )
        else:
            favourite.delete()

            messages.info(
                request,
                f"Removed {location.name} from saved parking.",
            )

    next_url = request.POST.get("next", "")

    if next_url.startswith("/") and not next_url.startswith("//"):
        return redirect(next_url)

    return redirect(location)


@login_required
# lets users add parking locations
def parking_create(request):
    form = CommunityParkingLocationForm(
        request.POST or None
    )

    if request.method == "POST" and form.is_valid():
        location = form.save(commit=False)

        location.submitted_by = request.user
        location.council_verified = False
        location.save()

        messages.success(
            request,
            "Parking location added.",
        )

        return redirect(location)

    return render(
        request,
        "parking/form.html",
        {
            "form": form,
            "heading": "Add parking location",
            "submit_label": "Add parking",
        },
    )


@login_required
# edits a parking location
def parking_edit(request, pk):
    location = get_object_or_404(
        active_locations(),
        pk=pk,
    )

    if not (
        request.user.is_staff
        or location.submitted_by_id == request.user.id
    ):
        messages.error(
            request,
            "You can only edit your own parking locations.",
        )

        return redirect(location)

    if request.user.is_staff:
        form = ParkingLocationForm(
            request.POST or None,
            instance=location,
        )
    else:
        form = CommunityParkingLocationForm(
            request.POST or None,
            instance=location,
        )

    if request.method == "POST" and form.is_valid():
        location = form.save(commit=False)

        if not request.user.is_staff:
            location.council_verified = False

        location.save()

        messages.success(
            request,
            "Parking location updated.",
        )

        return redirect(location)

    return render(
        request,
        "parking/form.html",
        {
            "form": form,
            "heading": "Edit parking location",
            "submit_label": "Save changes",
        },
    )


@login_required
# deletes a parking location
def parking_delete(request, pk):
    location = get_object_or_404(
        active_locations(),
        pk=pk,
    )

    if not (
        request.user.is_staff
        or location.submitted_by_id == request.user.id
    ):
        messages.error(
            request,
            "You can only delete your own parking locations.",
        )

        return redirect(location)

    if request.method == "POST":
        location.delete()

        messages.success(
            request,
            "Parking location deleted.",
        )

        return redirect("parking:dashboard")

    return render(
        request,
        "parking/delete.html",
        {
            "location": location,
        },
    )
