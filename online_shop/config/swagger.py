from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Online Shop API",
        default_version='v1',
        description="This is the API documentation for the Online Shop project. Here you can find all the endpoints and their descriptions.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@onlineshop.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# from drf_yasg.renderers import SwaggerUIRenderer
#
# class MySwaggerRenderer(SwaggerUIRenderer):
#     def get_customizations(self):
#         customizations = super().get_customizations()
#         customizations['displayOperationId'] = True
#         customizations['defaultModelExpandDepth'] = 2
#         return customizations
#
# urlpatterns = [
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0, renderer_classes=[MySwaggerRenderer]), name='schema-swagger-ui'),]

