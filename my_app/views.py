from django.shortcuts import render,get_object_or_404,reverse,redirect
from django.views import generic
from .models import Teacher, Student
from .forms import TeacherForm, StudentForm
from django.contrib import messages



# Create your views here.
class TeacherListView(generic.ListView):
    template_name = 'my_app/teacher_list.html'
    queryset = Teacher.objects.all()
    paginate_by = 4



class StudentListView(generic.ListView):
    template_name = 'my_app/student_list.html'
    queryset = Student.objects.all()
    paginate_by = 6
    # ordering = ['id']



class TeacherCreateView(generic.CreateView):
    template_name = 'my_app/teacher_form_create.html'
    form_class = TeacherForm


    def get_success_url(self):
        messages.success(self.request, ('New Teacher Added!!'))
        return reverse('teacher_list')



class TeacherUpdateView(generic.UpdateView):
    template_name = 'my_app/teacher_form_create.html'
    form_class = TeacherForm
    # queryset = Teacher.objects.all()


    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Teacher, id=id)


    def get_success_url(self):
        messages.success(self.request, ('Teacher information Updated!!'))
        return reverse('teacher_list')



class TeacherDeleteView(generic.DeleteView):
    template_name = 'my_app/teacher_delete.html'

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Teacher, id=id)

    def get_success_url(self):
        messages.success(self.request, ('Teacher id Deleted!!'))
        return reverse('teacher_list')



class StudentCreateView(generic.CreateView):
    template_name = 'my_app/student_form_create.html'
    form_class = StudentForm

    def get_success_url(self):
        messages.success(self.request, ('New Student Added!!'))
        return reverse('student_list')




class StudentUpdateView(generic.UpdateView):
    template_name = 'my_app/student_form_create.html'
    form_class = StudentForm

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Student, id=id)

    def get_success_url(self):
        messages.success(self.request, ('Student information Updated!!'))
        return reverse('student_list')



class StudentDetailView(generic.DetailView):
    template_name = 'my_app/student_detail.html'
    context_object_name = 'obj'

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Student, id=id)


class AboutView(generic.TemplateView):
    template_name = 'my_app/about.html'








class StudentDeleteView(generic.DeleteView):
    template_name = 'my_app/student_delete.html'
    form_class = StudentForm

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Student, id=id)

    def get_success_url(self):
        messages.success(self.request, ('Student id Deleted!!'))
        return reverse('student_list')
