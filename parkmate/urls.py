# url routes for the main project.

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("parking.urls")),
]

# custom error pages
handler400 = "parking.error_handlers.bad_request"
handler403 = "parking.error_handlers.permission_denied"
handler404 = "parking.error_handlers.page_not_found"
handler500 = "parking.error_handlers.server_error"
