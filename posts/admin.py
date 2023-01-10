from django.contrib import admin

from .models import StatusType, StatusCommentType
admin.site.register(StatusType)
admin.site.register(StatusCommentType)