from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from .views import CostApiView

urlpatterns = [
    path('api/v1/my-costs/', CostApiView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/my-costs/<int:pk>/', CostApiView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('api-auth/', include('rest_framework.urls')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
