from django.contrib import admin

from .models import Profile,candidates,votes_candidate

admin.site.register(Profile)
admin.site.register(candidates)
admin.site.register(votes_candidate)
