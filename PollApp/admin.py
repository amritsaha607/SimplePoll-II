from django.contrib import admin

from PollApp.models import Choice, Poll, User, Vote

# Register your models here.

admin.site.register(User)
admin.site.register(Choice)
admin.site.register(Poll)
admin.site.register(Vote)
