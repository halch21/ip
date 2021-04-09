from django.shortcuts import render
from rest_framework import viewsets
from .serializer import OrderSerializer, StaffSerializer, BookingSerializer, TypeRooomSerializer
from coworking.models import Staff, Booking, TypeRooom, Order 


class OrderViewset(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        order = Order.objects.all()
        return order


class StaffViewset(viewsets.ModelViewSet):
    serializer_class = StaffSerializer

    def get_queryset(self):
        staff = Staff.objects.all()
        return staff
 

class BookingViewset(viewsets.ModelViewSet):
    serializer_class = BookingSerializer

    def get_queryset(self):
        booking = Booking.objects.all()
        return booking


class TypeRooomViewset(viewsets.ModelViewSet):
    serializer_class = TypeRooomSerializer

    def get_queryset(self):
        typeRooom = TypeRooom.objects.all()
        return typeRooom


 