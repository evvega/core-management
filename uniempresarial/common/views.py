from django import http


def health_check(request):
    return http.HttpResponse()