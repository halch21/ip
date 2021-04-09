from coworking.models import Staff, Booking, TypeRooom, Order 
from rest_framework import serializers


class StaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields = ['id', 'name', 'surname', 'email', 'phone', 'post']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'price', 'booking', 'status', 'manager']


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ['id', 'date', 'number', 'customer', 'phone', 'type_room', 'period']


class TypeRooomSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeRooom
        fields = ['id', 'title', 'price']



 