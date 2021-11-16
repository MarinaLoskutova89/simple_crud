from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from measurements import views

router = routers.DefaultRouter()
router.register('project', views.ProjectViewSet, basename='project')
router.register('measurement', views.MeasurementViewSet, basename='measurement')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
]
