from django.urls import path
from . import views

urlpatterns = [
    # === index всего CRUD-приложения ===
    path('', views.CrudIndexView.as_view(), name='crud-index'),

    # === Person ===
    path('persons/',      views.PersonListView.as_view(),   name='person-list'),
    path('persons/add/',  views.PersonCreateView.as_view(), name='person-create'),
    path('persons/<int:pk>/',      views.PersonDetailView.as_view(), name='person-detail'),
    path('persons/<int:pk>/edit/', views.PersonUpdateView.as_view(), name='person-update'),
    path('persons/<int:pk>/del/',  views.PersonDeleteView.as_view(), name='person-delete'),

    # === Passport ===
    path('passports/',      views.PassportListView.as_view(),   name='passport-list'),
    path('passports/add/',  views.PassportCreateView.as_view(), name='passport-create'),
    path('passports/<int:pk>/',      views.PassportDetailView.as_view(), name='passport-detail'),
    path('passports/<int:pk>/edit/', views.PassportUpdateView.as_view(), name='passport-update'),
    path('passports/<int:pk>/del/',  views.PassportDeleteView.as_view(), name='passport-delete'),

    # === Author ===
    path('authors/',      views.AuthorListView.as_view(),   name='author-list'),
    path('authors/add/',  views.AuthorCreateView.as_view(), name='author-create'),
    path('authors/<int:pk>/',      views.AuthorDetailView.as_view(), name='author-detail'),
    path('authors/<int:pk>/edit/', views.AuthorUpdateView.as_view(), name='author-update'),
    path('authors/<int:pk>/del/',  views.AuthorDeleteView.as_view(), name='author-delete'),

    # === Book ===
    path('books/',      views.BookListView.as_view(),   name='book-list'),
    path('books/add/',  views.BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/',      views.BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/edit/', views.BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/del/',  views.BookDeleteView.as_view(), name='book-delete'),

    # === Course ===
    path('courses/',      views.CourseListView.as_view(),   name='course-list'),
    path('courses/add/',  views.CourseCreateView.as_view(), name='course-create'),
    path('courses/<int:pk>/',      views.CourseDetailView.as_view(), name='course-detail'),
    path('courses/<int:pk>/edit/', views.CourseUpdateView.as_view(), name='course-update'),
    path('courses/<int:pk>/del/',  views.CourseDeleteView.as_view(), name='course-delete'),

    # === Student ===
    path('students/',      views.StudentListView.as_view(),   name='student-list'),
    path('students/add/',  views.StudentCreateView.as_view(), name='student-create'),
    path('students/<int:pk>/',      views.StudentDetailView.as_view(), name='student-detail'),
    path('students/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student-update'),
    path('students/<int:pk>/del/',  views.StudentDeleteView.as_view(), name='student-delete'),
]
