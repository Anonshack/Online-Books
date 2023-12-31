from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static, settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Books, web-site after Anonymouse",
      default_version='v1',
      description="hello, clay",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="anonshack48@gmail.com"),
      license=openapi.License(name="Anons"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("todo/", include('app_todo.urls')),
    path("users/", include('users.urls')),
    path('', include('temp.urls')),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

