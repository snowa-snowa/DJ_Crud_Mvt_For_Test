from django.contrib import admin
from .models import Person, Passport, Author, Book, Course, Student

admin.site.register(Person)
admin.site.register(Passport)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Course)
admin.site.register(Student)
