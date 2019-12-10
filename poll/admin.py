from django.contrib import admin

from .models import Choice, Title


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class TitleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('title_text', 'pub_date')

    inlines = [ChoiceInline]


admin.site.register(Title, TitleAdmin)
