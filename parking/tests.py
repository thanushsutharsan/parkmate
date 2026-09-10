# Tests for the parking app.
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Favourite, ParkingLocation


class ParkMateTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="tester",
            password="pass12345",
        )
        self.location = ParkingLocation.objects.create(
            name="Test Car Park",
            address="High Street, Test Town",
            postcode="ME1 1AA",
            nation="england",
            local_authority="Test Council",
            latitude="51.380000",
            longitude="0.520000",
            tariff_info="£1.50 per hour",
            council_verified=False,
            submitted_by=self.user,
        )

    def test_home_page_loads(self):
        response = self.client.get(reverse("parking:home"))
        self.assertEqual(response.status_code, 200)

    def test_search_finds_parking_by_postcode(self):
        response = self.client.get(reverse("parking:list"), {"q": "ME1"})
        self.assertContains(response, "Test Car Park")

    def test_city_search_returns_all_matching_parking(self):
        ParkingLocation.objects.create(
            name="Bullring Parking - Birmingham",
            address="Bullring, Birmingham",
            postcode="B5 4BU",
            nation="england",
            local_authority="Birmingham City Council",
            latitude="52.477000",
            longitude="-1.894000",
            tariff_info="Check local signs",
        )
        ParkingLocation.objects.create(
            name="Digbeth Parking - Birmingham",
            address="Digbeth, Birmingham",
            postcode="B5 6DY",
            nation="england",
            local_authority="Birmingham City Council",
            latitude="52.475000",
            longitude="-1.885000",
            tariff_info="Check local signs",
        )
        response = self.client.get(
            reverse("parking:list"),
            {"q": "Birmingham"},
        )
        self.assertContains(response, "Bullring Parking - Birmingham")
        self.assertContains(response, "Digbeth Parking - Birmingham")

    def test_detail_page_loads(self):
        response = self.client.get(
            reverse("parking:detail", args=[self.location.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "£1.50 per hour")

    def test_map_page_loads_database_location(self):
        response = self.client.get(reverse("parking:map"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Car Park")

    def test_logged_in_user_can_save_parking(self):
        self.client.login(username="tester", password="pass12345")
        self.client.post(
            reverse("parking:toggle_favourite", args=[self.location.pk])
        )
        self.assertTrue(
            Favourite.objects.filter(
                user=self.user,
                parking=self.location,
            ).exists()
        )

    def test_logged_in_user_can_add_parking(self):
        self.client.login(username="tester", password="pass12345")
        response = self.client.post(
            reverse("parking:create"),
            {
                "name": "New Parking",
                "address": "Station Road, Test Town",
                "postcode": "ME2 2BB",
                "nation": "england",
                "local_authority": "Test Council",
                "latitude": "51.390000",
                "longitude": "0.530000",
                "parking_type": "car_park",
                "operator_name": "",
                "spaces_total": "20",
                "disabled_spaces": "2",
                "tariff_info": "£2 per hour",
                "charging_times": "8am to 6pm",
                "restrictions": "None supplied",
                "payment_info": "Card",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            ParkingLocation.objects.filter(name="New Parking").exists()
        )

    def test_user_can_register(self):
        response = self.client.post(
            reverse("parking:register"),
            {
                "username": "newuser",
                "email": "newuser@example.com",
                "password1": "StrongPass12345!",
                "password2": "StrongPass12345!",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_user_can_log_in_and_log_out(self):
        login_response = self.client.post(
            reverse("login"),
            {"username": "tester", "password": "pass12345"},
        )
        self.assertEqual(login_response.status_code, 302)

        logout_response = self.client.post(reverse("logout"))
        self.assertEqual(logout_response.status_code, 302)

    def test_user_can_remove_saved_parking(self):
        Favourite.objects.create(user=self.user, parking=self.location)
        self.client.login(username="tester", password="pass12345")
        self.client.post(
            reverse("parking:toggle_favourite", args=[self.location.pk])
        )
        self.assertFalse(
            Favourite.objects.filter(
                user=self.user,
                parking=self.location,
            ).exists()
        )

    def test_owner_can_edit_own_parking(self):
        self.client.login(username="tester", password="pass12345")
        response = self.client.post(
            reverse("parking:edit", args=[self.location.pk]),
            {
                "name": "Updated Car Park",
                "address": self.location.address,
                "postcode": self.location.postcode,
                "nation": self.location.nation,
                "local_authority": self.location.local_authority,
                "latitude": self.location.latitude,
                "longitude": self.location.longitude,
                "parking_type": "car_park",
                "operator_name": "",
                "spaces_total": "20",
                "disabled_spaces": "2",
                "tariff_info": "£2 per hour",
                "charging_times": "8am to 6pm",
                "restrictions": "None supplied",
                "payment_info": "Card",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.location.refresh_from_db()
        self.assertEqual(self.location.name, "Updated Car Park")

    def test_owner_can_delete_own_parking(self):
        self.client.login(username="tester", password="pass12345")
        response = self.client.post(
            reverse("parking:delete", args=[self.location.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            ParkingLocation.objects.filter(pk=self.location.pk).exists()
        )

    def test_other_user_cannot_edit_someone_elses_parking(self):
        other_user = User.objects.create_user(
            username="otheruser", password="pass12345"
        )
        self.client.login(username="otheruser", password="pass12345")
        response = self.client.post(
            reverse("parking:edit", args=[self.location.pk]),
            {
                "name": "Changed By Other User",
                "address": self.location.address,
                "postcode": self.location.postcode,
                "nation": self.location.nation,
                "local_authority": self.location.local_authority,
                "latitude": self.location.latitude,
                "longitude": self.location.longitude,
                "parking_type": "car_park",
                "operator_name": "",
                "spaces_total": "20",
                "disabled_spaces": "2",
                "tariff_info": "£2 per hour",
                "charging_times": "8am to 6pm",
                "restrictions": "None supplied",
                "payment_info": "Card",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.location.refresh_from_db()
        self.assertEqual(self.location.name, "Test Car Park")
        self.assertNotEqual(other_user, self.location.submitted_by)

    def test_other_user_cannot_delete_someone_elses_parking(self):
        User.objects.create_user(username="otheruser", password="pass12345")
        self.client.login(username="otheruser", password="pass12345")
        response = self.client.post(
            reverse("parking:delete", args=[self.location.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            ParkingLocation.objects.filter(pk=self.location.pk).exists()
        )
