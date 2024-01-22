from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenRefreshView

from erp_greenwich.auth.api.views import MyTokenObtainPairView
from erp_greenwich.users.views import HomeView, index

schema_view = get_schema_view(
    openapi.Info(
        title="GAE EndUser API",
        default_version="v1",
        description="Greenwich Application Ecosystem end user api documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="cuonglieu3256@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=[
        path("api/", include("config.api_router")),
        path("oauth/", include("oauth2_provider.urls", namespace="oauth2_provider")),
    ],
)

urlpatterns = [
    path("", index, name="index"),
    path("home/", HomeView.as_view(), name="home"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("erp_greenwich.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
    path(
        "swagger.json",
        schema_view.without_ui(cache_timeout=0),
        name="enduser_schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="enduser-schema-swagger-ui",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()

# API URLS
urlpatterns += [
    # API base url
    # Oauth token
    path("oauth/", include("oauth2_provider.urls", namespace="oauth2_provider")),
    path("auth/token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/", include("config.api_router")),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
