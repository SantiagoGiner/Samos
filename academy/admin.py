from django.contrib import admin
from .models import *


admin.site.register(Course, CourseAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(File, FileAdmin)
