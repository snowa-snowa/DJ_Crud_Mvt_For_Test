from django.views import generic
from .models import Profile, ProfileExtra,Blog, Entry,Tag, Article
from django.views.generic import TemplateView
from django.utils import timezone

class MvtIndexView(TemplateView):
    template_name = 'mvt_index.html'
    extra_context = {'now': timezone.now()}

# Profile & ProfileExtra
class ProfileListView(generic.ListView):
    model = Profile

class ProfileDetailView(generic.DetailView):
    model = Profile

class ProfileExtraListView(generic.ListView):
    model = ProfileExtra

class ProfileExtraDetailView(generic.DetailView):
    model = ProfileExtra

# Blog & Entry
class BlogListView(generic.ListView):
    model = Blog

class BlogDetailView(generic.DetailView):
    model = Blog

class EntryListView(generic.ListView):
    model = Entry

class EntryDetailView(generic.DetailView):
    model = Entry

# Tag & Article
class TagListView(generic.ListView):
    model = Tag

class TagDetailView(generic.DetailView):
    model = Tag

class ArticleListView(generic.ListView):
    model = Article

class ArticleDetailView(generic.DetailView):
    model = Article
