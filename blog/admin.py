from django.contrib import admin

from .models import Tag, Author, Post, Comment

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email")

class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date")
    list_display = ("title", "date", "author")
    prepopulated_fields = {"slug":("title",)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "user_email", "short_text", "post")

    def short_text(self,obj):
        return obj.text[:30] + "...." if len(obj.text)>30 else obj.text


admin.site.register(Tag)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

