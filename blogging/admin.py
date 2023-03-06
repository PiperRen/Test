from django.contrib import admin
from blogging.models import Post, Category


# Register your models here.
# admin.site.register(Post)
# admin.site.register(Category)


class CategoryInline(admin.TabularInline):
    model = Category.posts.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    inlines = [CategoryInline,]
    fields = ('title', 'text', 'author', 'published_date')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    fields = ('name', 'description')
    exclude = ('posts',)
