from django.contrib import admin
from .models import Students

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('stdId', 'stdName', 'stdYear', 'stdCourse')


admin.site.register(Students, StudentAdmin)