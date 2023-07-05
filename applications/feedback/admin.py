from django.contrib import admin

from applications.feedback.models import CRating, DRating

# Register your models here.
admin.site.register(DRating)
admin.site.register(CRating)