from django.contrib import admin
from .models import Category, Memes
from django.contrib.auth.models import Group, User

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=("name",)
    search_fields=("name",)


@admin.register(Memes)
class MemesAdmin(admin.ModelAdmin):
    list_display=('title','tags','category')
    search_fields=('title',)
    list_filter=('category',)
    save_on_top=True


