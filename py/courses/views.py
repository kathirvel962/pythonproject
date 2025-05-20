from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course, Lesson, UserProgress

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lessons = course.lessons.all()
    
    if request.user.is_authenticated:
        progress, created = UserProgress.objects.get_or_create(
            user=request.user,
            course=course
        )
        completed_lessons = progress.completed_lessons.all()
    else:
        progress = None
        completed_lessons = []

    return render(request, 'courses/course_detail.html', {
        'course': course,
        'lessons': lessons,
        'progress': progress,
        'completed_lessons': completed_lessons
    })

@login_required
def lesson_detail(request, course_id, lesson_id):
    course = get_object_or_404(Course, id=course_id)
    lesson = get_object_or_404(Lesson, id=lesson_id, course=course)
    progress, created = UserProgress.objects.get_or_create(
        user=request.user,
        course=course
    )

    if request.method == 'POST':
        user_solution = request.POST.get('solution', '')
        if user_solution.strip() == lesson.solution.strip():
            progress.completed_lessons.add(lesson)
            messages.success(request, 'Exercise completed successfully!')
        else:
            messages.error(request, 'Solution is incorrect. Please try again.')

    return render(request, 'courses/lesson_detail.html', {
        'course': course,
        'lesson': lesson,
        'progress': progress
    })

@login_required
def mark_lesson_complete(request, course_id, lesson_id):
    if request.method == 'POST':
        course = get_object_or_404(Course, id=course_id)
        lesson = get_object_or_404(Lesson, id=lesson_id, course=course)
        progress, created = UserProgress.objects.get_or_create(
            user=request.user,
            course=course
        )
        progress.completed_lessons.add(lesson)
        messages.success(request, 'Lesson marked as complete!')
    return redirect('lesson_detail', course_id=course_id, lesson_id=lesson_id)
