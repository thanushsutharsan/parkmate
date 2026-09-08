# custom error pages for the site.

from django.shortcuts import render


# renders the shared error template
def _render_error(request, status_code, title, message):
    return render(
        request,
        "errors/error.html",
        {
            "status_code": status_code,
            "error_title": title,
            "error_message": message,
        },
        status=status_code,
    )


# handles bad requests
def bad_request(request, exception):
    return _render_error(
        request,
        400,
        "We could not process that request",
        "Check the information you entered and try again.",
    )


# handles permission errors
def permission_denied(request, exception):
    return _render_error(
        request,
        403,
        "You do not have permission to view this page",
        "Return to ParkMate or sign in with the correct account.",
    )


# handles missing pages
def page_not_found(request, exception):
    return _render_error(
        request,
        404,
        "That page could not be found",
        "The page may have moved, or the address may be incorrect.",
    )


# handles server errors
def server_error(request):
    return _render_error(
        request,
        500,
        "ParkMate is temporarily unavailable",
        "Please try again in a moment.",
    )