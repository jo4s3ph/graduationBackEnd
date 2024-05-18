from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

# Setting up the Swagger schema view for API documentation
schema_view = get_schema_view(
    openapi.Info(
        title="MASSAR API",  # Title of the API
        default_version='v1',  # API version
        description="API for an educational game.",  # Description of the API
        terms_of_service="",  # Terms of service URL
        contact=openapi.Contact(email=""),  # Contact information
        license=openapi.License(name=""),  # License information
    ),
    public=True,
    permission_classes=[permissions.AllowAny]  # Permissions for accessing the schema
)

# Defining URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URLs
    path('api/authentication/', include('authentication.urls')),  # Authentication app URLs
    path('api/system_admin/', include('system_admin.urls')),  # System admin app URLs
    path('api/faculty_member/', include('faculty_member.urls')),  # Faculty member app URLs
    path('api/student/', include('student.urls')),  # Student app URLs

    # URLs for Swagger UI and Redoc
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Serving media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
