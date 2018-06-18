from django.contrib import admin
from snippets.models import Snippet

class BbsAdmin(admin.ModelAdmin):
    list_display=('title','code','created',)

admin.site.register(Snippet, BbsAdmin)