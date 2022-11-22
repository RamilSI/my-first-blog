from django.contrib import admin
from .models import Post
# from .models import Schema, Cat, Client



# class PostAdmin(Post):
#     model = Post
#     list_display = ['title', 'author', 'text', 'summary', 'category', 'created_date', 'published_date', 'is_published', 'slug']
#     prepopulated_fields = {'slug': ('title',)}
# admin.site.register(Schema)
# admin.site.register(Cat)
# admin.site.register(Client)

admin.site.register(Post)
