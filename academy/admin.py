from django.contrib import admin
from .models import *


admin.site.register(Course, CourseAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Video, VideoAdmin)
