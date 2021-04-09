from django.conf.urls import url, include
from .views import StaffViewset, OrderViewset, BookingViewset, TypeRooomViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('staff', StaffViewset, basename='staff')
router.register('order', OrderViewset, basename='order')
router.register('booking', BookingViewset, basename='booking')
router.register('typeroom', TypeRooomViewset, basename='typeroom')


urlpatterns = [
    url('', include(router.urls)),


]