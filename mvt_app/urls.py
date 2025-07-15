from django.urls import path
from . import views

urlpatterns = [
    # === index всего MVT-приложения ===
    path('', views.MvtIndexView.as_view(), name='mvt-index'),

    # === Profile ===
    path('profiles/',      views.ProfileListView.as_view(),   name='profile-list'),
    path('profiles/<int:pk>/', views.ProfileDetailView.as_view(), name='profile-detail'),

    # === ProfileExtra ===
    path('profileextras/',      views.ProfileExtraListView.as_view(),   name='profileextra-list'),
    path('profileextras/<int:pk>/', views.ProfileExtraDetailView.as_view(), name='profileextra-detail'),

    # === Blog ===
    path('blogs/',      views.BlogListView.as_view(),   name='blog-list'),
    path('blogs/<int:pk>/', views.BlogDetailView.as_view(), name='blog-detail'),

    # === Entry ===
    path('entries/',      views.EntryListView.as_view(),   name='entry-list'),
    path('entries/<int:pk>/', views.EntryDetailView.as_view(), name='entry-detail'),

    # === Tag ===
    path('tags/',      views.TagListView.as_view(),   name='tag-list'),
    path('tags/<int:pk>/', views.TagDetailView.as_view(), name='tag-detail'),

    # === Article ===
    path('articles/',      views.ArticleListView.as_view(),   name='article-list'),
    path('articles/<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
]
