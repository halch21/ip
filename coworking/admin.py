from django.contrib import admin
from .models import Booking, TypeRooom, Order, Staff
from import_export.admin import ImportExportModelAdmin

class BookingAdmin(ImportExportModelAdmin):
    list_display = ('number', 'customer', 'type_room', 'date', 'period')
    list_display_links = ('number', )
    list_filter = ("type_room", )
    search_fields = ("customer__startswith",)
    pass

class StaffAdmin(ImportExportModelAdmin):
    list_display = ('surname', 'name', 'post', 'email', 'phone')
    list_display_links = ('surname', )
    list_filter = ("post", )
    search_fields = ("surname__startswith",)
    pass

def no_paid(modeladmin, request, queryset):
    queryset.update(status=0)
no_paid.short_description = "Изменить статус на 'Не оплачен' "

def paid(modeladmin, request, queryset):
    queryset.update(status=1)
paid.short_description = "Изменить статус на 'Оплачен' "

class OrderAdmin(ImportExportModelAdmin):
    list_display = ('booking', 'manager', 'price', 'status')
    list_display_links = ('booking', )
    list_filter = ("status", )
    actions = [no_paid, paid]
    pass




admin.site.register(Booking, BookingAdmin)
admin.site.register(TypeRooom)
admin.site.register(Order, OrderAdmin)
admin.site.register(Staff, StaffAdmin)

