from django.http import HttpRequest
from django.shortcuts import render
from django.views.decorators.cache import never_cache

from homepage.const import libraries, demos
from homepage.cookies import get_debug_cookie_name, get_debug_cookie_expiration
from homepage.services import SessionService


@never_cache
def myverify(request: HttpRequest):
    """
    Render the homepage
    """

    session_service = SessionService()
    session_service.start_session(session=request.session)

    template = "homepage/myverify.html"

    # Enable adding ?debug=true to the URL to show additional information
    show_debug_info = request.GET.get("debug") == "true"

    response = render(request, template, {})

    if show_debug_info:
        response.set_cookie(
            key=get_debug_cookie_name(),
            value="true",
            expires=get_debug_cookie_expiration(),
        )

    return response
