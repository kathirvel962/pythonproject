from django.contrib import admin
from .models import Course, Lesson, UserProgress

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'language')
    list_filter = ('language', 'created_at')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')
    list_filter = ('course',)
    search_fields = ('title', 'content')
    ordering = ('course', 'order')

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'progress_percentage', 'last_accessed')
    list_filter = ('course', 'user')
    search_fields = ('user__username', 'course__title')
