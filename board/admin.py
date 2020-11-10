from django.contrib import admin

# Register your models here.
from board.models import Board, Employees

# admin.site.register(Board)
admin.site.register(Employees)

class BoardAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['id', 'title', 'userid', 'regdate']
    list_filter = ['title', 'userid', 'regdate']

admin.site.register(Board, BoardAdmin)