from django.db import connection
from django.http import HttpResponse


def index(request):
    """
    Determines if app is available
    """

    return HttpResponse("")


def databases(request):
    """
    Determines if DB is up & running
    """

    connection.ensure_connection()
    return HttpResponse("")
