from django.contrib import admin

from posts.models import Post, Comment, Follow


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'text',
                    'pub_date',
                    'author',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'post',
                    'author',
                    'text',
                    'created')
    search_fields = ('text',)
    list_filter = ('created', 'author')
    empty_value_display = '-пусто-'


class FollowAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'user',
                    'author')
    search_fields = ('author',)
    list_filter = ('author',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)
