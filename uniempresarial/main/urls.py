"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from common.views import health_check
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('djoser.urls.base')),
    url(r'^auth/', include('djoser.urls.authtoken')),
    url(r'^health_check/', health_check),
]

# Load core enabled modules dynamic
for core_module in settings.APP_MODULES:
    module = __import__(core_module, globals(), locals(), ['urls'], 0)
    urls = module.urls
    urlpatterns.append(url(r'^{0}/'.format(core_module), include(urls.router.urls)))


# Swagger URLs
schema_view = get_swagger_view(title='Core API Uniempresarial',)
urlpatterns.extend([
    url(r'^api/docs/$', schema_view)
])

# DRF URLs
urlpatterns.extend([
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
])

# DEBUG URLS
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
