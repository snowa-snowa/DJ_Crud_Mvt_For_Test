from django.contrib import admin
from .models import Profile, ProfileExtra, Blog, Entry, Tag, Article

admin.site.register(Profile)
admin.site.register(ProfileExtra)
admin.site.register(Blog)
admin.site.register(Entry)
admin.site.register(Tag)
admin.site.register(Article)
