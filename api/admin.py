from django.contrib import admin
from .models import User, Table, Month, Estate, Report

admin.site.register(User)
admin.site.register(Table)
admin.site.register(Month)
admin.site.register(Estate)
admin.site.register(Report)