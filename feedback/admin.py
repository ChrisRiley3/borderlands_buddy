from django.contrib import admin
from .models import Feedback


class feedbackAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'feedback',
    )


admin.site.register(Feedback, feedbackAdmin)
