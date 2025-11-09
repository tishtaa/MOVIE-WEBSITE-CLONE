from django.contrib import admin
from .models import CustomUser,Profile,Movie,Video

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Profile)
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'age_limit', 'is_showcase']
    list_filter = ['age_limit', 'is_showcase']
admin.site.register(Video)