from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django.utils import timezone
from .models import Person, Passport, Author, Book, Course, Student

class CrudIndexView(TemplateView):
    template_name = 'crud_index.html'
    extra_context = {'now': timezone.now()}

# === Person & Passport ===
class PersonListView(generic.ListView):
    model = Person

class PersonDetailView(generic.DetailView):
    model = Person

class PersonCreateView(generic.CreateView):
    model = Person
    fields = '__all__'
    success_url = reverse_lazy('person-list')

class PersonUpdateView(generic.UpdateView):
    model = Person
    fields = '__all__'
    success_url = reverse_lazy('person-list')

class PersonDeleteView(generic.DeleteView):
    model = Person
    success_url = reverse_lazy('person-list')


class PassportListView(generic.ListView):
    model = Passport

class PassportDetailView(generic.DetailView):
    model = Passport

class PassportCreateView(generic.CreateView):
    model = Passport
    fields = '__all__'
    success_url = reverse_lazy('passport-list')

class PassportUpdateView(generic.UpdateView):
    model = Passport
    fields = '__all__'
    success_url = reverse_lazy('passport-list')

class PassportDeleteView(generic.DeleteView):
    model = Passport
    success_url = reverse_lazy('passport-list')


# === Author & Book ===
class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author

class AuthorCreateView(generic.CreateView):
    model = Author
    fields = '__all__'
    success_url = reverse_lazy('author-list')

class AuthorUpdateView(generic.UpdateView):
    model = Author
    fields = '__all__'
    success_url = reverse_lazy('author-list')

class AuthorDeleteView(generic.DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')


class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book

class BookCreateView(generic.CreateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('book-list')

class BookUpdateView(generic.UpdateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('book-list')

class BookDeleteView(generic.DeleteView):
    model = Book
    success_url = reverse_lazy('book-list')


# === Course & Student ===
class CourseListView(generic.ListView):
    model = Course

class CourseDetailView(generic.DetailView):
    model = Course

class CourseCreateView(generic.CreateView):
    model = Course
    fields = '__all__'
    success_url = reverse_lazy('course-list')

class CourseUpdateView(generic.UpdateView):
    model = Course
    fields = '__all__'
    success_url = reverse_lazy('course-list')

class CourseDeleteView(generic.DeleteView):
    model = Course
    success_url = reverse_lazy('course-list')


class StudentListView(generic.ListView):
    model = Student

class StudentDetailView(generic.DetailView):
    model = Student

class StudentCreateView(generic.CreateView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('student-list')

class StudentUpdateView(generic.UpdateView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(generic.DeleteView):
    model = Student
    success_url = reverse_lazy('student-list')
