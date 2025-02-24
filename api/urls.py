from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParentViewSet, SchoolViewSet, DriverViewSet, BusRouteViewSet

router = DefaultRouter()
router.register(r'parents', ParentViewSet)
router.register(r'schools', SchoolViewSet)
router.register(r'drivers', DriverViewSet)
router.register(r'busroutes', BusRouteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]