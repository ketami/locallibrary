from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, NavigationMenu, NavigationTree

admin.site.register(Genre)

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
admin.site.register(Author, AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorator

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','status','borrower','due_back')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )

@admin.register(NavigationTree)
class NavigationTreeAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent','order')

class NavigationTreeInline(admin.TabularInline):
    model = NavigationTree
    extra = 0
    list_filter = (
        ('nav_menu', admin.RelatedOnlyFieldListFilter),
    )

@admin.register(NavigationMenu)
class NavigationMenuAdmin(admin.ModelAdmin):
    inlines = [NavigationTreeInline]