from rest_framework import viewsets, status
from .models import Parent, School, Driver, BusRoute
from .serializers import ParentSerializer, SchoolSerializer, DriverSerializer, BusRouteSerializer
from utils.entity_body import create_response

class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return create_response(response.data, "Parents retrieved successfully")

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return create_response(response.data, "Parent created successfully", status_code=status.HTTP_201_CREATED)

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return create_response(response.data, "Schools retrieved successfully")

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return create_response(response.data, "School created successfully", status_code=status.HTTP_201_CREATED)

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return create_response(response.data, "Drivers retrieved successfully")

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return create_response(response.data, "Driver created successfully", status_code=status.HTTP_201_CREATED)

class BusRouteViewSet(viewsets.ModelViewSet):
    queryset = BusRoute.objects.all()
    serializer_class = BusRouteSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return create_response(response.data, "Bus routes retrieved successfully")

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return create_response(response.data, "Bus route created successfully", status_code=status.HTTP_201_CREATED)