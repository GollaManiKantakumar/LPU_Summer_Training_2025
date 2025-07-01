from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Course

class CourseListView(ListView):
    model = Course
    template_name = 'educationmanagement/course_list.html'
    context_object_name = 'courses'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'educationmanagement/course_detail.html'
    context_object_name = 'course'

class CourseCreateView(CreateView):
    model = Course
    fields = ['title', 'description', 'instructor_name', 'duration']
    template_name = 'educationmanagement/course_form.html'
    success_url = reverse_lazy('course-list')

class CourseUpdateView(UpdateView):
    model = Course
    fields = ['title', 'description', 'instructor_name', 'duration']
    template_name = 'educationmanagement/course_form.html'
    success_url = reverse_lazy('course-list')

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'educationmanagement/course_delete.html'
    success_url = reverse_lazy('course-list')
