from django.conf import settings
from apps.ecommerce import models

def RequestExposerMiddleware(get_response):
    def middleware(request):
        if request.session.get('lang') is None:
            request.session['lang'] = 'uk'
        models.exposed_request = request
        response = get_response(request)
        return response
    return middleware

def RequestLangMiddleware(get_response):
    def middleware(request):
        if request.session.get('lang') is None:
            request.session['lang'] = 'uk'
        response = get_response(request)
        return response
    return middleware

