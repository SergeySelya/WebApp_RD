from django.contrib import admin
from .models import Post_0, Post_1, Post_2, Post_3, Post_4, Post_5


@admin.register(Post_0, Post_1, Post_2, Post_3, Post_4, Post_5)
class UserPost(admin.ModelAdmin):

    actions = ['delete_info']

    def delete_info(self, request, queryset):
        queryset.update(total_paid=0)
    delete_info.short_description = "Del info about total_paid"

    list_display = ('fio', 'post', 'post_head', 'wages', 'total_paid')
    # list_display_links = ('post_head',)
    list_filter = ['post']


# admin.site.register(Post_0)
# admin.site.register(Post_1)
# admin.site.register(Post_2)
# admin.site.register(Post_3)
# admin.site.register(Post_4)
# admin.site.register(Post_5)
